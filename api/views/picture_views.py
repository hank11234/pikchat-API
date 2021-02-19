from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.picture import Picture
from ..serializers import PictureSerializer, UserSerializer, PictureAllSerializer

# Create your views here.
class PicturesAll(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = PictureAllSerializer
    def get(self, request):
        """Index All request"""
        pictures = Picture.objects.all()
        data = PictureSerializer(pictures, many=True).data
        return Response({ 'pictures': data })

class Pictures(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = PictureSerializer
    def get(self, request):
        """Index request"""
        # Get all the pictures:
        # pictures = picture.objects.all()
        # Filter the pictures by owner, so you can only see your owned pictures
        pictures = Picture.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = PictureSerializer(pictures, many=True).data
        return Response({ 'pictures': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['picture']['owner'] = request.user.id
        # Serialize/create picture
        picture = PictureSerializer(data=request.data['picture'])
        # If the picture data is valid according to our serializer...
        if picture.is_valid():
            # Save the created picture & send a response
            picture.save()
            return Response({ 'picture': picture.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(picture.errors, status=status.HTTP_400_BAD_REQUEST)

class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the picture to show
        picture = get_object_or_404(Picture, pk=pk)
        serializer = PictureSerializer(picture)
        
        # Run the data through the serializer so it's formatted
        data = serializer.data
        # Only want to show owned pictures?
        if not request.user.id == picture.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this picture')

        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        # Locate picture to delete
        picture = get_object_or_404(Picture, pk=pk)
        # Check the picture's owner agains the user making this request
        if not request.user.id == picture.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this picture')
        # Only delete if the user owns the  picture
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['picture'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['picture'].get('owner', False):
            del request.data['picture']['owner']

        # Locate picture
        # get_object_or_404 returns a object representation of our picture
        picture = get_object_or_404(Picture, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == picture.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this picture')

        # Add owner to data object now that we know this user owns the resource
        request.data['picture']['owner'] = request.user.id
        # Validate updates with serializer
        data = PictureSerializer(picture, data=request.data['picture'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

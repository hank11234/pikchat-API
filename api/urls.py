from django.urls import path
from .views.picture_views import Pictures, PictureDetail, PicturesAll
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.comment_views import Comments, CommentDetail

urlpatterns = [
  	# Restful routing
    path('pictures/all/', PicturesAll.as_view(), name='pictures_all'),
    path('pictures/', Pictures.as_view(), name='pictures'),
    path('pictures/<int:pk>/', PictureDetail.as_view(), name='picture_detail'),
    path('comments/', Comments.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]

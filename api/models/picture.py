from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Picture(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100, blank=True)
  picture = models.CharField(max_length=100000, blank=True)
  description = models.CharField(max_length=100000, blank=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"{self.title}: {self.description}"

  def as_dict(self):
    """Returns dictionary version of Picture models"""
    return {
        'id': self.id,
        'title': self.title,
        'picture': self.picture,
        'description': self.description
    }

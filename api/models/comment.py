from django.db import models
from django.contrib.auth import get_user_model

class Comment(models.Model):
  comment = models.CharField(max_length=100000)
  owner = models.ForeignKey(
      get_user_model(),
      related_name='comments',
      on_delete=models.CASCADE
  )
  picture_id = models.ForeignKey('Picture', on_delete=models.CASCADE)

  def __str__(self):
        return self.comment

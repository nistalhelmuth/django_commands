from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255, default="")
  content = models.CharField(max_length=255, default="")
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

class UserLikePost(models.Model):
  user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
  post =models.ForeignKey(Post, related_name='post',on_delete=models.CASCADE)

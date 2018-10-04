from django.db import models

# Create your models here.

class Users(models.Model):
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)

class UserLikeUser(models.Model):
  follower = models.ForeignKey(Users, related_name='follower' ,on_delete=models.CASCADE)
  user = models.ForeignKey(Users, related_name='user' ,on_delete=models.CASCADE)


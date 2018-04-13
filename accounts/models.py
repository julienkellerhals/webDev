from django.db import models

# Dev eveveveve
class Dev(models.Model):
    user_name = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    projects = models.PositiveIntegerField() # hmmm
    status = models.PositiveSmallIntegerField()
    profile_pic = models.CharField(max_length=30) # path 

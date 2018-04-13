from django.db import models

# Dev eveveveve
class Dev(models.Model):
    user_name = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length)
    email = models.EmailField()
    password = models.CharField(max_length=25)
 

from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return '@{}'.format(self.username)

#for class.User fields, attrb, methods, etc: https://docs.djangoproject.com/en/2.2/ref/contrib/auth/


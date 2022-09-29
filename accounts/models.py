from django.db import models
from django.contrib import auth


class User(auth.models.User ,auth.models.PremissionsMixin):

    def __str__(self):
        
        return str(self.username)
# Create your models here.

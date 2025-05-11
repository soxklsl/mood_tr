from django.db import models

class Users(models.Model):
    user_login = models.TextField()
    password = models.TextField()
    password_salt = models.TextField()
    
    
from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 75, blank=False, unique=True)
    email = models.EmailField(unique=True, blank=True)
    password = models.CharField(max_length=30, blank=False)
    image = models.ImageField(default='fallback.png', blank=True)
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    picture = models.ImageField(upload_to='profile', blank=True, null=True)


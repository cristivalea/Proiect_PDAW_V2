
from django.contrib.auth.models import AbstractUser

from Magazin_Online import models


class User(AbstractUser):
    address = models.TextField()
    phone = models.CharField(max_length=20)

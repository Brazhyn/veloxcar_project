from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    profile_image = models.ImageField(upload_to='accounts/images', default='default/user.jpg', blank=True, null=True)
    address = models.CharField(max_length=130, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.username}, {self.email}"
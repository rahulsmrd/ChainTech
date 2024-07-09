from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User as MainUser

# Create your models here.

class Register(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return f"@{self.username}"


class Profile(models.Model):
    owner = models.ForeignKey(MainUser, related_name='UserProfile', on_delete=models.CASCADE, unique=True)
    profile_picture = models.FileField(upload_to='media', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class HomePage(models.Model):
    owner = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='HomePage')
    title = models.CharField(max_length=255)
    pic = models.FileField(upload_to='media', blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.title)[:15]

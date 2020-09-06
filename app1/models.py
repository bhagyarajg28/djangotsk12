from django.db import models
from django.contrib.auth.models import User
from random import choice
from django.core.validators import MaxValueValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Age = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    UniqueId = models.CharField(max_length=6, unique=True, blank=False, null=False)
    Image = models.ImageField(upload_to='images')

    def Unique_Id(self):
        a = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(3)])
        b = ''.join([choice('0123456789') for i in range(3)])
        self.UniqueId = b + a

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

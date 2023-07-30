from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator 




class CustomUser(AbstractUser):
    age= models.PositiveBigIntegerField(null=True,blank=True)
    lock_status = models.BooleanField(default=False)
    lock_count = models.PositiveIntegerField(default=7,validators=[MaxValueValidator(7),MinValueValidator(0)])
    user_is_sender = models.BooleanField(default=False)
    user_is_reciever = models.BooleanField(default=False)
    user_locked_with = models.CharField(max_length=125,null=True,blank=True)
    lock_exist = models.BooleanField(default=False)
    lock_published = models.BooleanField(default=False)

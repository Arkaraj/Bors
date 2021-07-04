from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class User (models.Model):
    name = models.CharField(max_length=50, null=False, default="")


class Dog (models.Model):
    name = models.CharField(max_length=100, null=False, default="")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='User', null=True)
    breed = models.CharField(max_length=20, default="")
    weight = models.FloatField(default=0.0)
    gender = models.CharField(max_length=1, default="M")
    colour = models.CharField(max_length=50, default="brown")
    description = models.CharField(max_length=500, default="Its a cute dog")

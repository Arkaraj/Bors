from django.db import models
# from django.db.models.deletion import CASCADE

# Create your models here.


class User (models.Model):
    name: models.CharField(max_length=50)


class Dog (models.Model):
    name: models.CharField(max_length=100)
    # owner: models.ForeignKey(User, on_delete=models.CASCADE)
    breed: models.CharField(max_length=20)
    weight: models.FloatField(default=0.0)
    gender: models.CharField(max_length=1)
    colour: models.CharField(max_length=50)
    description: models.CharField(max_length=500)

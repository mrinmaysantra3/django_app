from os import name
from django.db import models

# Create your models here.

#base_player is the table name where players data is stored

class Player(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    score=models.IntegerField()


from django.db import models

# Create your models here.

class Passenger(models.Model):
    firstname=models.CharField(max_length=33)
    lastname=models.CharField(max_length=33)

    def __str__(self):
        return self.firstname

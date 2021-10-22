from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}-{self.surname}'
# Create your models here.

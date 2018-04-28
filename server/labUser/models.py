from django.db import models

# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=20)
    userId=models.IntegerField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.userName

from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
class employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    studcode=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    oragnization=models.CharField(max_length=200)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    

# Create your models here.

from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)
    address=models.TextField(max_length=150)
    select_state=(
        ('India','India'),
        ('Japan','Japan'),
        ('China','China')
    )
    state=models.CharField(max_length=15,choices=select_state)
    zip=models.IntegerField()
    mark=models.BooleanField(default=False)

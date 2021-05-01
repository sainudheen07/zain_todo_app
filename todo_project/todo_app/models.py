from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priourity=models.IntegerField()
    date=models.DateField(default=datetime.date.today())


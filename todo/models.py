from django.db import models

# Create your models here.


class ToDo_List(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=200)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
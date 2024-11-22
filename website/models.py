from django.db import models


# Create your models here.
class Books(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='books/')
    
    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title 


class Lectures(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='lectures/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lectures')
    
    def __str__(self):
        return self.title        
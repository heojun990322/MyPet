from typing import Any, Dict, Tuple
from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="", blank=True, null=True)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
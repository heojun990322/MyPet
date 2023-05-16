from typing import Any, Dict, Tuple
from django.db import models
import os
from django.conf import settings

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="", blank=True, null=True)
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
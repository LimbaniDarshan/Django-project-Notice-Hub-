from django.db import models
from django.contrib.auth.models import User    

class Noticehub(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notice_name = models.CharField(max_length=100)
    notice_description = models.TextField()
    

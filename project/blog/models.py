from django.db import models
from django.conf import settings
 
User = settings.AUTH_USER_MODEL

# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
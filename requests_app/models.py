from django.db import models 
from django.contrib.auth.models import User 
 
class Request(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100) 
    description = models.TextField() 
 
class RequestMessage(models.Model): 
    request = models.ForeignKey(Request, related_name='messages', on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
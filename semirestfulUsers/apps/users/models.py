from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name']="Name must not be empty"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Email must be valid"
        exists=User.objects.filter(email=postData['email'])
        if exists:
            errors['emailUsed']="Email is taken"
        return errors
class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)
    objects=UserManager()
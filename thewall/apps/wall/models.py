from django.db import models

# Create your models here.
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'^[a-zA-z]')
# Create your models here.

class UserManager(models.Manager):
    def validateData(self,postData):
        errors={}
        if len(postData['first_name']) < 2:
            errors['first_name']="First name Must be greater than 2 characters"
        if len(postData['last_name']) <2:
            errors['last_name']="Last name must be greater than 2 characters"
        if not NAME_REGEX.match(postData['first_name']):
            errors['firstRegex']="First name must be only letters"
        if not NAME_REGEX.match(postData['last_name']):
            errors['lastRegex']="last name must be only letters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Email must be valid"
        if not postData['password']==postData['confirm']:
            errors['password']="Passwords must match"
        if len(postData['password'])<8:
            errors['pwlength']="Password must be more than 8 characters"
        exists=User.objects.filter(email=postData['email'])
        if exists:
            errors['emailUsed']="Email is taken"
        return errors
    def validate_login(self,postData):
        user = User.objects.get(email=postData['email'])
        errors={}
        if bcrypt.checkpw(postData['password'].encode(), user.pw_hash.encode()):
            return errors
        else:
            errors['error']="Email or password incorrect"
            return errors                   

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    pw_hash=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)
    objects=UserManager()

class Message(models.Model):
    message=models.TextField()
    user_messages= models.ForeignKey(User,related_name='messages')
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)

class Comment(models.Model):
    comment=models.TextField()
    messages_comments=models.ForeignKey(Message,related_name='comments')
    user_comments= models.ForeignKey(User,related_name='users')
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)
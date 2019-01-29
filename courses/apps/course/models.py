from django.db import models

# Create your models here.

class courseManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name']="Course name must be more than 5 Characters"
        if len(postData['desc']) <15:
            errors['desc']="Course Description must be longer than 15 characters"
        return errors
class Course(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now= True)
    objects=courseManager()
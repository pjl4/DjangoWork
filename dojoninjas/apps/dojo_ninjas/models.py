from django.db import models

# Create your models here.

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.TextField(default="Default option")

class Ninja(models.Model):
    dojo_location=models.ForeignKey(Dojo,on_delete=models.PROTECT, related_name="dojos")
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
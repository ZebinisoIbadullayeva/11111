from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=50)
    jshr = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20,default='0',blank=True)

    def __str__(self):
        return self.name
    

class Keys(models.Model):
    token = models.CharField(max_length=150)
    user = models.ForeignKey(Person,on_delete=models.CASCADE,related_name='token')

    def __str__(self) -> str:
        return self.user.name
        
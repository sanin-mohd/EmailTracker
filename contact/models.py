from django.db import models
from django.db.models.fields import UUIDField
from django.db.models.fields.related import ForeignKey
import uuid
# Create your models here.

class EmailEventDatabase(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    email=models.EmailField(max_length = 254)
    time=models.DateTimeField(auto_now_add=True)
    no_of_opening=models.IntegerField(default=-1)
    last_opened_time=models.DateTimeField(auto_now=True)
    last_used_ip=models.CharField(max_length=100,null=True)
    last_location=models.CharField(max_length=1000,default="--")
    class Meta:
        ordering = ['-last_opened_time']
    def __str__(self):
        return str(self.email)+"  >>>  "+str(self.id)

class Ip(models.Model):
    email_event=models.ForeignKey(EmailEventDatabase,on_delete=models.CASCADE)
    ip=models.CharField(max_length=100)
    location=models.CharField(max_length=1000,default='--')






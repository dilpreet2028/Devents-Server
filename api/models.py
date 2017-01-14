from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserLogin(models.Model):
	username=models.CharField(max_length=50,default=" ")
	email=models.CharField(max_length=50,primary_key=True)
	gcm=models.CharField(max_length=200,blank=True,null=True)
	class Meta:
		db_table="userlogin"

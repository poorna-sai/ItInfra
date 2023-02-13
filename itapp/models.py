from django.db import models
from datetime import datetime
# Create your models here.


class Itdb(models.Model):
	Device_Name = models.CharField(max_length = 100 , blank = True)
	Device_Serial = models.CharField(max_length = 100 , blank = True)
	Issued_To = models.CharField(max_length = 100 , blank = True)
	other = models.TextField(default = "no remarks")
	Remarks  = models.TextField(default = "no remarks")

class Complaints(models.Model):
	 Name = models.CharField(max_length = 100 , blank = True)
	 Id_Numbeer = models.CharField(max_length = 100 , blank = True)
	 Class = models.CharField(max_length = 50 , blank = True)
	 Description = models.TextField(default = "no remarks")
	 Device_Name = models.CharField(max_length = 50 , blank = True)
	 date = models.DateTimeField(blank=True  , default=datetime.now )
	 videoproof = models.FileField(null=True, blank=True, upload_to = 'videos/')


class SolvedComplaints(models.Model):
	 Name = models.CharField(max_length = 100 , blank = True)
	 Id_Numbeer = models.CharField(max_length = 100 , blank = True)
	 Class = models.CharField(max_length = 50 , blank = True)
	 Description = models.TextField(default = "no remarks")
	 Device_Name = models.CharField(max_length = 50 , blank = True)
	 date = models.DateTimeField(blank=True  , default=datetime.now )
	 videoproof = models.FileField(null=True, blank=True, upload_to = 'videos/')
	 Rating  = models.CharField(max_length = 100 , blank = True)
	 suggestions = models.TextField(default = "No Suggestions")


class UserModel(models.Model):
	username = models.CharField(max_length = 100  , blank = True)
	email  = models.EmailField(max_length=70,blank=True,unique=True)
	forget_password_token = models.CharField(max_length=100 ,default = "vsdfjsd558dsdfsr5rr")

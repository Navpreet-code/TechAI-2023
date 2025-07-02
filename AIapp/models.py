from django.db import models

# Create your models here.
class person(models.Model):
	First_name=models.CharField(max_length=50)
	Last_name=models.CharField(max_length=50)
	def __str__(self):
		return self.First_name

class FAQ(models.Model):
	Ques=models.TextField()
	Ans=models.TextField()
	def __str__(self):
		return self.Ques

class MyReview(models.Model):
	Title=models.CharField(max_length=10000)
	Message=models.TextField()

class Contactus(models.Model):
	Name=models.CharField(max_length=10000)
	Email=models.EmailField()
	Subject=models.CharField(max_length=10000)
	Message=models.TextField()

class HelpandSupport(models.Model):
	Title=models.CharField(max_length=10000)
	Message=models.TextField()		

class user_register(models.Model):
	Name=models.CharField(max_length=10000,blank=True,null=True)
	Email=models.EmailField(blank=True,null=True)
	Password=models.CharField(max_length=10000,blank=True,null=True)
	Age=models.CharField(max_length=10000,blank=True,null=True)
	Gender=models.CharField(max_length=10000,blank=True,null=True)
	DOB=models.CharField(max_length=10000,blank=True,null=True)
	PhoneNo=models.CharField(max_length=10000,blank=True,null=True)
	Profile=models.ImageField(upload_to="imgs",blank=True, null=True)
	def __str__(self):
		return self.Name

class Blog(models.Model):
	Name=models.CharField(max_length=10000)
	Image=models.ImageField()
	Writter=models.CharField(max_length=10000)
	Description=models.TextField()
	def __str__(self):
		return self.Name

class video(models.Model):
	Title=models.CharField(max_length=1000)
	Video=models.FileField()
	def __str__(self):
		return self.Title

class category(models.Model):
	category_name=models.CharField(max_length=100,primary_key=True)
	def __str__(self):
		return self.category_name

class structure(models.Model):
	category_name=models.ForeignKey(category, on_delete=models.CASCADE)
	tool_Name=models.CharField(max_length=100)
	tool_Image=models.ImageField(upload_to="data",blank=True)
	tool_Description=models.TextField()
	tool_link=models.URLField(max_length=500)


class initiative(models.Model):
	Title=models.CharField(max_length=100)
	Image=models.ImageField(upload_to="data",blank=True)
	Description=models.TextField()
	def __str__(self):
		return self.Title


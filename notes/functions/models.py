from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
    
class AI(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JAVA(models.Model):
    title=models.CharField(max_length=60)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DM(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PD(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class IME(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SE(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DS(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SD(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NS(models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="Files")
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
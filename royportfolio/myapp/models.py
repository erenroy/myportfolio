from django.db import models

# Create your models here.
# Starting og Blog Section 
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    thumbleimage =  models.ImageField(upload_to ='blogpic',blank=True,null=True)  # pic must be 600x400
    blogimg = models.ImageField(upload_to ='blogpic',blank=True,null=True)  # pic must be 600x400
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=130)
    
    def __str__(self):
        return self.title


class Project(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    content = models.TextField()
    fimage =  models.ImageField(upload_to ='projectpic',blank=True,null=True)  # pic must be 600x400
    simage =  models.ImageField(upload_to ='projectpic',blank=True,null=True)  # pic must be 600x400
    timage =  models.ImageField(upload_to ='projectpic',blank=True,null=True)  # pic must be 600x400
    forthimage =  models.ImageField(upload_to ='projectpic',blank=True,null=True)  # pic must be 600x400
    timeStamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=130)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    reason = models.CharField(max_length=500)

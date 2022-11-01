from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, null=True, blank=True)
    logo = models.ImageField(upload_to='image/company/logo')

    def __str__(self):
        return self.name

class Advocates(models.Model):
    company = models.ForeignKey(Company ,on_delete=models.SET_NULL, blank=True, null=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='image/advocates')
    twitter = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.username
    
from django.db import models

# Create your models here.


class Advocates(models.Model):
    profile_pic = models.ImageField(upload_to='image/advocates')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.username
    
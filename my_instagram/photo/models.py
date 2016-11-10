from django.db import models
from member.models import MyUser

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField('photo/origin_photo')
    author = models.ForeignKey(MyUser)
    content = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('PhotoTag')


class PhotoTag(models.Model):
    title = models.CharField(max_length=20)


class PhotoReply(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(MyUser)
    reply = models.TextField(max_length=150)

from django.db import models
from member.models import MyUser
from django.conf import settings

__all__ = [
    'Photo',
    'PhotoTag',
    'PhotoComment',
    'PhotoLike'
]


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='photo/origin_photo')
    author = models.ForeignKey(MyUser)
    content = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('PhotoTag')
    like_users = models.ManyToManyField(
        MyUser,
        through='PhotoLike',
        related_name='photo_set_like_users'
    )


class PhotoTag(models.Model):
    title = models.CharField(max_length=20)


class PhotoComment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(MyUser)
    reply = models.TextField(max_length=150)


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(MyUser)
    created_date = models.DateField(auto_now_add=True)

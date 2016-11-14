from django.db import models
from member.models import MyUser
from django.conf import settings
from django.urls import reverse

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
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('photo:photo_list')

    def __str__(self):
        return self.content

    def to_dict(self):
        ret = {
            'id': self.id,
            'image': self.photo.url,
            'author': self.author.id,
            'content': self.content,
            'commentList': [comment.to_dict() for comment in self.photocomment_set.all()],
        }
        return ret


class PhotoTag(models.Model):
    title = models.CharField(max_length=20)


class PhotoComment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(MyUser)
    reply = models.TextField(max_length=150)

    def to_dict(self):
        ret = {
            'id': self.id,
            'photo': self.photo.id,
            'author': self.author.id,
            'reply': self.reply,
        }
        return ret


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(MyUser)
    created_date = models.DateField(auto_now_add=True)

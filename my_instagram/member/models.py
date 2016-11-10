from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user_profile', blank=True, null=True)
    like_photos = models.ManyToManyField('photo.Photo')
    following_users = models.ManyToManyField('self', symmetrical=False,
                                             related_name='follow_users', through='Following',)
    block_users = models.ManyToManyField('self', symmetrical=False,
                                         related_name='user_set_block',)
    objects = CustomUserManager()

    def __str__(self):
        return self.username


    def follow(self, user):
        instance, created = Following.objects.get_or_create(
            follower=self,
            followee=user
        )
        return instance

    def unfollow(self, user):
        Following.objects.filter(follower=self, followee=user).delete()

    def get_all_following(self):
        return self.following_users.all()

    def get_all_followee(self):
        return self.follow_users.all()


class Following(models.Model):
    follower = models.ForeignKey(MyUser, related_name='user_set_follower')
    followee = models.ForeignKey(MyUser, related_name='user_set_followee')
    created_date = models.DateField(auto_now_add=True)
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserManager(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(upload_to='user_profile', blank=True, null=True)
    # like_photos = models.ManyToManyField('photo.Photo',
    #                                      through='Photo.PhotoLike',
    #                                      related_name='user_set_like_photos')
    following_users = models.ManyToManyField('self', symmetrical=False,
                                             related_name='follow_users', through='Relationship',)
    block_users = models.ManyToManyField('self', symmetrical=False,
                                         related_name='user_set_block',)
    objects = CustomUserManager()


    def __str__(self):
        return self.username


    def follow(self, user):
        instance, created = Relationship.objects.get_or_create(
            follower=self,
            followee=user
        )
        return instance


    def block(self, user):
        self.block_users.add(user)

    def unblock(self, user):
        self.block_users.remove(user)

    def unfollow(self, user):
        Relationship.objects.filter(follower=self, followee=user).delete()


    def get_all_following(self):
        return self.following_users.all()


    def get_all_followee(self):
        return self.follow_users.all()


    def friends(self):
        return self.following_users.filter(following_users=self)


    def is_friends(self, user):
        return user in self.following_users.all().filter(follow_users=self)
        # Following.objects.filter(
        #     Q(follower=self, followee=user) &
        #     Q(followee=self, follower=user)).exists()


class Relationship(models.Model):
    follower = models.ForeignKey(MyUser, related_name='relationship_follower')
    followee = models.ForeignKey(MyUser, related_name='relationship_followee')
    created_date = models.DateField(auto_now_add=True)
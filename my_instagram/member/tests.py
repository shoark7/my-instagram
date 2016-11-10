from django.test import TestCase, LiveServerTestCase
from .models import MyUser

# Create your tests here.
class FollowTest(LiveServerTestCase):
    def create_user(self, username, last_name, first_name):
        return MyUser.objects.create_user(
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

    def test_create_user(self):
        print("test create user")
        u1 = self.create_user('u1', '방','민아')
        u2 = self.create_user('u2', 'dl','ㅇ하녕')
        u3 = self.create_user('u3', '박','성환')


    def test_follow_user(self):
        print("test create user")
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', 'dl', 'ㅇ하녕')
        u3 = self.create_user('u3', '박', '성환')

        u2.follow(u1)
        u3.follow(u2)
        u3.follow(u1)

        print(u2.follow_users.all())
        print(u3.follow_users.all())
        print()
        print(u1.followers.all())


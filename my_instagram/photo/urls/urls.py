from django.conf.urls import url
from photo import views


urlpatterns = [
    url(r'list', views.photo_list, name='photo_list'),
]
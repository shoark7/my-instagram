from django.conf.urls import url
from .. import apis


urlpatterns = [
    url(r'^photo/add/$', apis.photo_add, name='photo_add'),
]
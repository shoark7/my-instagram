from django.conf.urls import url, include
from member import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base/common.html'), name='base'),
    url(r'^login/$', views.login_form,  name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
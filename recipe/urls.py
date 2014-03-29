from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views

from recipe import views


urlpatterns = patterns('',
	url(r'test', views.test, name='test'),
	url(r'^$', views.index, name='index'),
)


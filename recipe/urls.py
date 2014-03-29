from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views

from recipe import views


urlpatterns = patterns('',
	url(r'search', views.search, name='search'),
	url(r'^recipe/(?P<number>\d+)/$', views.recipe, name='recipe'),
	url(r'^$', views.index, name='index'),
)


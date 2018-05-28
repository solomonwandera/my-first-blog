from django.conf.urls import url
from . import views
from django.urls import path,include


urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	path('^post/new/$',views.post_new, name='post_new'),
	path('^post/(?P<pk>\d+)/edit/$',views.post_edit,name='post_edit'),
]
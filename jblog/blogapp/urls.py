from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$', views.main_page, name='main_page'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
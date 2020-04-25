from django.conf.urls import include, url
from educoderapp import views

urlpatterns = [
	url(r'^$', views.index),
	#url(r'^create2/$',views.create2),
	url(r'^register1/$',views.register1),
	url(r'^register/$',views.register),
	url(r'^login1/$',views.login1),
	url(r'^login/$',views.login),  
	#url(r'^delete(\S+)/$',views.show_arg),
	url(r'^index_sec/$',views.index_sec),
	#url(r'^test_get/$',views.show_test),
	#url(r'^sub/$',views.sub),
	url(r'^logout/$',views.logout)
]
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^posts$',views.posts, name='index'),
	url(r'^post$',views.post, name='index'),
	url(r'^comments$',views.comments, name='index'),
	url(r'^comment$',views.comment, name='index'),
	url(r'^$',views.search, name='index'),
	]
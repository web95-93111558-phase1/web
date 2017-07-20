from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^auth/',include('users.urls')),
	url(r'^blog/',include('blogs.urls')),
	url(r'^search/blog',include('blogs.urls')),
    url(r'^admin/', admin.site.urls),
]
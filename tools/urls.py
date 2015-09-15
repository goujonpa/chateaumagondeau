from django.conf.urls import include, url
from tools import views

urlpatterns = [
    url(r'^login/$', views.tools_login, name='tools_login'),
    url(r'^news/$', views.tools_news, name='tools_news'),
    url(r'^$', views.tools_home, name='tools_home'),
]

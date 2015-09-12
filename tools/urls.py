from django.conf.urls import include, url
from tools import views

urlpatterns = [
    url(r'^news$', views.news_tool, name='news_tool'),
]

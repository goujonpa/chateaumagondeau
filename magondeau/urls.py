"""magondeau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin

# REST imports
from rest_framework import routers

# Home imports
from home import urls as home_urls

# Tools imports
from tools import urls as tools_urls

# News imports
from news.serializers import NewSerializer
from news.viewsets import NewViewSet

# Routers
router = routers.DefaultRouter()
router.register(r'new', NewViewSet)

# URL patterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tools/', include(tools_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', include(home_urls)),
]

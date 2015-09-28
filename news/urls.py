# DJANGO
from django.conf.urls import include, url

# REST
from rest_framework.urlpatterns import format_suffix_patterns

# VIEWS
from news.views import NewsList, NewsDetail

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', NewsDetail.as_view()),
    url(r'^$', NewsList.as_view()),
    # url(r'^article/(?P<id>\d+)$', views.article, name='news_article'),
    # url(r'$', views.home, name='news_home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

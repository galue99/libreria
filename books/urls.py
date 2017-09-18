__author__ = 'edgar'

from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^books/$', views.books_list),
    #url(r'^books/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
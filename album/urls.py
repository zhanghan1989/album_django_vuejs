from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    #url(r'^index/$', views.index),

    #url(r'^(?P<album_id>[0-9]+)/$', views.album_page),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_page, name='album_page'),

    #url(r'^edit/$', views.album_edit_page, name='album_edit_page'),
    url(r'^edit/(?P<album_id>[0-9]+)/$', views.album_edit_page, name='album_edit_page'),
    
    url(r'^edit/action$', views.album_edit_action_page, name='album_edit_action'),
]
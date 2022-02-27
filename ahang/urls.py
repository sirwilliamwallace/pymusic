from django.urls import re_path
from . import views

app_name='music'
urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^upload/$', views.upload_music_form, name='upload'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^signup/$', views.register, name='register'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_user, name='logout'),
    re_path(r'^edame/(?P<id>[0-9]{1,1000})*/$', views.ahang_detail, name='detail'),
    # url(r'^edame/(?P<id>[0-9]{1,1000})*/$', views.ahang_detail, name='detail'),
]

# url(r'^(?P<ahang_esm>[\w+][^/]*)$', views.ahang_detail, name='detail'),
# r'^(?P<id>[0-9]{1,})+/(?P<ahang_esm>[\w+][^/]*)$'

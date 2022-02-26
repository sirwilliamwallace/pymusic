from django.conf.urls import url
from . import views

app_name='music'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^upload$', views.upload_music_form, name='upload'),
    url(r'^search$', views.search, name='search'),
    url(r'^signup$', views.register, name='register'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^edame/(?P<id>[0-9]{1,1000})*/$', views.ahang_detail, name='detail'),
]

# url(r'^(?P<ahang_esm>[\w+][^/]*)$', views.ahang_detail, name='detail'),
# r'^(?P<id>[0-9]{1,})+/(?P<ahang_esm>[\w+][^/]*)$'

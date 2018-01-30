from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from website import views
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'logout/^$', views.home, name='logout'),
    url(r'^$', views.home, name='home'),

]
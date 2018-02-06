from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from website import views
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^user/logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'logout/^$', views.user, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'user/$',views.user,name='user'),
    url(r'signup/$',views.signup, name='signup'),
]
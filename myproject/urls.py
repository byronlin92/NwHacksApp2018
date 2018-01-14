"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    #POSTS
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^posts/new$', views.post_new, name='post_new'),
    url(r'^posts/(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/(?P<post_pk>\d+)/update$', views.post_update, name='post_update'),
    url(r'^posts/(?P<post_pk>\d+)/schedule', views.post_schedule, name='post_schedule'),
    url(r'^account/(?P<user_username>\w+)/scheduledPosts', views.scheduled_posts, name='scheduled_posts'),

    #ACCOUNTS
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    #INFO TABS
    url(r'^howItWorks/$', views.howItWorks, name='howItWorks'),
    url(r'^serviceConnections/$', views.serviceConnections, name='serviceConnections'),
    url(r'^meetOurTeam/$', views.meetOurTeam, name='meetOurTeam'),
    url(r'^reviews/$', views.reviews, name='reviews'),

    url(r'^account/(?P<user_username>\w+)/details/$', account_views.account_detail, name='account_detail'),
    url(r'^account/(?P<user_username>\w+)/update/$', account_views.account_update, name='account_update'),
    url(r'^account/(?P<user_username>\w+)/password/$', account_views.password_change, name='password_change'),

    url(r'^admin/', admin.site.urls),

    #PROFILE
    url(r'^profile/(?P<profile_pk>\d+)/details/$', account_views.profile_detail, name='profile_detail'),
    url(r'^profile/(?P<profile_pk>\d+)/update/$', account_views.profile_update, name='profile_update')

]

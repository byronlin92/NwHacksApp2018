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

    url(r'^admin/', admin.site.urls),

    # SIGN UP SCREEN
    url(r'^signup/$', account_views.signup, name='signup'),

    #LOGIN SCREEN
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login')

]

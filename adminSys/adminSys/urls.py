"""
URL configuration for adminSys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enroll import views

#import the decotrator of login required
"""before starting server run migration command"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.user_dashboard,name='dashboard'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('userdetail/<int:id>',views.user_detail,name='userdetail'),
    path('set/',views.setcookie,name='setcookie'),
    path('get/',views.getcookie,name='getcookie'),
    path('del/',views.delcookie,name='delcookie'),    
    # """for session frameword"""
    path('sets/',views.setsession,name='setsession'),    
    path('gets/',views.getsession,name='getsession'),    
    path('dels/',views.delsession,name='delsession'),    
]
"""
CACHE VIEW FUNCTION SEPARATELY FOR EACH URL 
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('profile/',cache_page(60)(views.user_profile),name='profile'),
    
    ]"""
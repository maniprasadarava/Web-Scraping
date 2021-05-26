"""webscrapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user  import views as user
from admin1 import views  as admins
from newsApp import views as news
from core import views as weather

urlpatterns = [
    path('admin1/', admin.site.urls),
    path('index/',user.index,name='index'),
    path('admn1/', admins.adminlogin, name='admn1'),
    path('userdetails/', admins.userdetails, name='userdetails'),
    path('adminloginentered/', admins.adminloginentered, name='adminloginentered'),
    path('activateuser/', admins.activateuser, name='activateuser'),
    path('storecsvdata/',admins.storecsvdata1,name='storecsvdata'),
    path('scrapping/',admins.scrapping,name='scrapping'),
    path('logout/', admins.logout, name='logout'),


    path('user/',user.userlogin,name='user'),
    path('userpage/',user.userpage,name='userpage'),
    path('userregister/',user.userregister,name='userregister'),
    path('userlogincheck/',user.userlogincheck,name='userlogincheck'),
    path('search/',user.search,name='search'),
    path('searchresult/',user.searchresult,name='searchresult'),
    path('wbscrapp/',user.wbscrapp,name='wbscrapp'),
    path('fpkart/',user.fpkart,name='fpkart'),
    path('jobsearch/',user.jobsearch,name='jobsearch'),

    path('nnews/',news.nindex,name='nnews'),
    path('weather/', weather.home, name='weather'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

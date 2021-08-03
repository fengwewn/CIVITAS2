"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from . import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getspeech/', views.getspeech1),
    path('speech/', views.speech1),
    path('getweather/',views.getweather1),
    path('getdate/',views.getdate1),
    path('islogin/',views.islogin1),
    path('login/',views.login1),
    path('register/',views.register1),
    path('assess/',views.assess1),
    path('hotspeech/',views.hotspeech1),
    path('siwei/',views.siwei),
    path('logout/',views.logout1),
    path('upload-avatar/',user.upload_avatar),
    path('getavatar/',user.get_avatar),
    path('test.html',views.test),
]

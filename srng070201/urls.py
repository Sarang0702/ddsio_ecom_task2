"""srng070201 URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views
from srng070201 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('login/',views.userlogin,name="login"),
    path('register/',views.register,name="register"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('smartphone/',views.smartphone,name="smartphone"),
    path('laptop/',views.laptop,name="laptop"),
    path('camera/',views.camera,name="camera"),
    path('profile/',views.profile,name="profile"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('addtocart/',views.addtocart,name="addtocart"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

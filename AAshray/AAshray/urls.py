"""AAshray URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('F1signin.html', views.login1, name='login1'),
    path('F2signin.html', views.login2, name='login2'),
    path('F4signin.html', views.login4, name='login4'),
    path('F5signin.html', views.login5, name='login5'),
    path('F7signin.html', views.login7, name='login7'),
    path('F8signin.html', views.login8, name='login8'),
    path('feedback.html', views.feedback, name='feedback'),
    path('volunteer-registration.html', views.volRegistration, name='volunteer-registration'),
    path('needvol-regestration.html', views.needVolReg, name='needvol-regestration'),
    path('shop-registration.html', views.ShopReg, name='shop-registration'),
    path('order-regestration.html', views.CustReg, name='order-regestration'),
    path('plasma-registration.html', views.PlasmaReg, name='plasma-registration'),
    path('needplasma-regestration.html', views.NeedPlasmaReg, name='needplasma-regestration'),
    path('volunteer-page.html', views.volunteer, name='volunteer'),
    path('needvol-page.html', views.needvolunteer, name='needvolunteer'),
    path('precautionary-page.html', views.pre, name='precautionary-page'),
    path('Regshop-page.html', views.shop, name='Regshop-page'),
    path('order-page.html', views.orderpage, name='order-page'),
    path('anti-dep-page.html', views.anti, name='anti-dep-page'),
    path('donor-page.html', views.donor, name='donor-page'),
    path('needplasma-page.html', views.needplasma, name='needplasma-page'),
    path('about-us.html', views.about, name='about'),


]

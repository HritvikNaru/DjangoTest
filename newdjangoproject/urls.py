"""newdjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from course import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cor/", include("course.urls")),
    path("fee/", include("fees.urls")),
    path("stuinfo/<int:pk>", views.student_detail),
    path("stucreate", views.stucreate),
    path("signin", views.signin),
    path("register", views.register),
    path("showform", views.showform),
    path("contactdetails", views.contactdetails),
    path("shopping", views.shopping),
    path("cart", views.addtocarts),
    path("showcart", views.showcart),
    path("cartdelete", views.cartdelete),
    path("placeorder", views.ordersplaced),
    path("showorder", views.showorders),
        


] 
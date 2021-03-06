"""totale URL Configuration

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
from django.urls import path
from commerce_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage.as_view(), name='index'),
    path('about/',views.Aboutpage.as_view(),name='about'),
    path('contact/',views.Contactpage.as_view(),name='contact'),
    path('courses/',views.Coursespage.as_view(),name='courses'),
    path('teacher/',views.Teacherpage.as_view(),name='teacher'),
    path('blog/',views.Blogpage.as_view(),name='blog'),
]

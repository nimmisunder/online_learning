from django.contrib import admin
from django.urls import path,include
from .import views,AdminVews
urlpatterns = [
    path('', views.home, name="home"),

]


# //url for admin

urlpatterns = [
    path('admins', AdminVews.home, name="home"),
    path('testimonials/', AdminVews.testimonials, name="testimonials"),

]
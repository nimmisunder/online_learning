from django.contrib import admin
from django.urls import path,include
from .import views,AdminVews
from django.contrib.auth.views import LoginView



# //url for admin

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', LoginView.as_view(template_name='admins/login.html'), name='login'),
    path('adminshome', AdminVews.home, name="adminshome"),
    path('testimonials/', AdminVews.testimonials, name="testimonials"),
    path('add-testimonial/', AdminVews.add_testimonial, name='add_testimonial'),


]
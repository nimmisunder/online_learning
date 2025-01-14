from django.shortcuts import render
from .models import Testimonial

def home(request):
    return render(request, 'admins/index.html')

def testimonials(request):
    return render(request, 'admins/testimonials.html')

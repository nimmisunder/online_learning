from django.shortcuts import render
from .models import Testimonial

def home(request):
    testimonials = Testimonial.objects.all()

    return render(request, 'courses/index.html', {'testimonials': testimonials})

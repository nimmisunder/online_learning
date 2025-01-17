from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Testimonial

def login_view(request):
    print("Accessed login_view")
    if request.user.is_authenticated:
        return redirect('adminshome')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'You are logged in successfully!')
            return redirect('adminshome')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'admins/login.html', {'form': form})

# @login_required
def home(request):
    print("Accessed home view")
    return render(request, 'adminshome')


def testimonials(request):
    testimonials_list = Testimonial.objects.all()
    return render(request, 'admins/testimonials.html', {'testimonials': testimonials_list})

def add_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        message = request.POST.get('message')
        image = request.FILES.get('image')  # Handles uploaded files
        
        # Save the new testimonial to the database
        Testimonial.objects.create(
            name=name,
            title=title,
            message=message,
            image=image
        )
        
        # Optional: Add a success message
        messages.success(request, "Testimonial added successfully!")
        return redirect('testimonials')  # Redirect to the testimonials page

    return render(request, 'admins/testimonials.html')
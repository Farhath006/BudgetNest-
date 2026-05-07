from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username and not email and not password:
            messages.error(request, 'Please enter all fields.')
            return redirect('signup')

        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully.')
        return redirect('login')
    return render(request,'accounts/signup.html')

@login_required
@never_cache
def dashboard(request):
    return render(request,'accounts/dashboard.html')

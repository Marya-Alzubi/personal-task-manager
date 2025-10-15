from django.shortcuts import render

# Create your views here.
# accounts_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Login failed. Please check username/password.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

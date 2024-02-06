from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm


def authenticate_and_login(request, username, password):
    authenticated_user  = authenticate(request, username=username, password=password)
    if authenticated_user is not None:
        login(request, authenticated_user)
        return True
    return False

class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user.set_password(raw_password)
            user.is_active = True
            user.save()
            
            if authenticate_and_login(request, username, raw_password):
                return redirect('blog:index')
            
        return render(request, "accounts/register.html", {'form': form})


class LoginView(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            if authenticate_and_login(request, username, password):
                return redirect('blog:index')
            
        return render(request, 'accounts/login.html', {'form': form})
        

def user_logout(request):
    logout(request)
    return redirect('blog:index')

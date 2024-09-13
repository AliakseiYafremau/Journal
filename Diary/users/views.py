from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from users.forms import LoginForm
from users.models import CustomUser

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if not CustomUser.objects.filter(username=username).exists():
                new_user = CustomUser.objects.create_user(username, password)
                django_login(request, new_user)
                return render(request, 'users/register.html')
            form.add_error('username', 'Username is already taken')
    else:
        form = LoginForm()
    return render(request, 'users/register.html', context={'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = CustomUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                django_login(request, user)
                return redirect('home')
            form.add_error('username', 'Credentials are invalid')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', context={'form': form})


def logout(request):
    django_logout(request)
    return redirect('login')


def index(request):
    return render(request, 'users/index.html')
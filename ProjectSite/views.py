from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def view_home(request):
    return render(request, 'ProjectSite/home.html')


def view_about(request):
    return render(request, 'ProjectSite/about.html')


def view_contacts(request):
    return render(request, 'ProjectSite/contacts.html')


def view_events(request):
    return render(request, 'ProjectSite/events.html')


def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
    return render(request, 'ProjectSite/login.html')


def view_logout(request):
    logout(request)
    return redirect('login')

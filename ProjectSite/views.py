from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import render, redirect
from ProjectSite.forms import LoginForm, SignUpForm


def view_home(request):
    return render(request, 'ProjectSite/home.html')


def view_about(request):
    return render(request, 'ProjectSite/about.html')


def view_contacts(request):
    return render(request, 'ProjectSite/contacts.html')


def view_events(request):
    return render(request, 'ProjectSite/events.html')


def view_login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_ThirdParty:
                login(request, user)
                return redirect('home')
            else:
                msg = 'invalid credentials'

        else:
            msg = 'error validating form'
    return render(request, 'ProjectSite/login.html', {'form': form, 'msg': msg})


def view_logout(request):
    logout(request)
    return redirect('login')


def view_register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'

    else:
        form = SignUpForm()
    return render(request, 'ProjectSite/register.html', {'form': form, 'msg': msg})

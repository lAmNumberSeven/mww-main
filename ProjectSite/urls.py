from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name="home"),
    path('events', views.view_events, name="events"),
    path('about', views.view_about, name="about"),
    path('contacts', views.view_contacts, name="contacts"),
    path('login', views.view_login, name="login"),
    path('logout', views.view_logout, name="logout")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('top100', views.top, name="top100"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact")
]

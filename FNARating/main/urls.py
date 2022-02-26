from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('top100', views.top),
    path('about', views.about),
    path('contact', views.contact)
]
#body { background-image: url("{% static 'img/background.jpg'%}"); }
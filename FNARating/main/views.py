from django.shortcuts import render
from main.scripts.drawer import get_background

# Create your views here.


def index(request):
    background = get_background()
    return render(request, 'main/index.html', {'bg_name': background})


def about(request):
    background = get_background()
    return render(request, 'main/about.html', {'bg_name': background})


def contact(request):
    background = get_background()
    return render(request, 'main/contact.html', {'bg_name': background})


def top(request):
    background = get_background()
    return render(request, 'main/top.html', {'bg_name': background})

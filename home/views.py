from django.shortcuts import render


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def home_about(request):
    """A view to return the home_about page"""
    return render(request, 'home/home_about.html')

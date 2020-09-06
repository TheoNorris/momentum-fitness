from django.shortcuts import render
import os


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def home_about(request):
    context = {
        'api_key': os.environ.get('GOOGLE_MAPS_API_KEY')
    }
    """A view to return the home_about page"""
    return render(request, 'home/home_about.html', context)

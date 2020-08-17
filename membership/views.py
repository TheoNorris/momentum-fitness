from django.shortcuts import render
from products.models import Product


def membership(request):
    """A view to return the membership page"""
    return render(request, 'membership/membership.html')

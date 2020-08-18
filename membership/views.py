from django.shortcuts import render
from products.models import Product


def membership(request):
    products = Product.objects.filter(category__name='Membership')

    context = {
        'products': products,
    }
    """A view to return the membership page"""
    return render(request, 'membership/membership.html',  context)

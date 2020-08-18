from django.shortcuts import render
from products.models import Product


def membership(request):
    products = Product.objects.filter(category='Membership')

    context = {
        'products': products,
    }
    """A view to return the membership page"""
    return render(request, context, 'membership/membership.html')

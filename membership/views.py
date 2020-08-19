from django.shortcuts import render
from products.models import Product


def membership(request):
    products = Product.objects.filter(category__name='Membership')

    context = {
        'products': products,
    }
    """A view to return the membership page"""
    return render(request, 'membership/membership.html',  context)


def members_only(request):
    """A view to return the members only page"""
    return render(request, 'membership/members_only.html')

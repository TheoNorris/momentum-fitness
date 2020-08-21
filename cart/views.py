from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """A view to return the shopping cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """"Add a quantity of the specified product to the cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size_or_flavour = None
    if 'product_variant' in request.POST:
        size_or_flavour = request.POST['product_variant']
    cart = request.session.get('cart', {})

    if size_or_flavour:
        if item_id in list(cart.keys()):
            if size_or_flavour in cart[item_id]['items_by_variant'].keys():
                cart[item_id]['items_by_variant'][size_or_flavour] += quantity
                messages.success(request, f'Updated {size_or_flavour.title()} {product.name} quantity \
                to {cart[item_id]["items_by_variant"][size_or_flavour]}')
            else:
                cart[item_id]['items_by_variant'][size_or_flavour] = quantity
                messages.success(request, f'Added {size_or_flavour.title()}\
                     {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_variant': {size_or_flavour: quantity}}
            messages.success(request, f'Added {size_or_flavour.title()} \
                {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            if not product.category.name == 'Membership':
                messages.success(request, f'Updated {product.name} quantity \
                    {cart[item_id]}')
        else:
            cart[item_id] = quantity
            if not product.category.name == 'Membership':
                messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def edit_cart(request, item_id):
    """"A view to edit products in the cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size_or_flavour = None
    if 'product_variant' in request.POST:
        size_or_flavour = request.POST['product_variant']
    cart = request.session.get('cart', {})

    if size_or_flavour:
        if quantity > 0:
            cart[item_id]['items_by_variant'][size_or_flavour] = quantity
            messages.success(request, f'Updated {size_or_flavour.title()}{product.name} quantity \
                to {cart[item_id]["items_by_variant"][size_or_flavour]}')
        else:
            del cart[item_id]['items_by_variant'][size_or_flavour]
            if not cart[item_id]['items_by_variant']:
                cart.pop(item_id)
                messages.success(request, f'Removed {size_or_flavour.title()}\
                     {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity \
                {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.info(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """"Remove the item from the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    size_or_flavour = None
    if 'product_variant' in request.POST:
        size_or_flavour = request.POST['product_variant']
    cart = request.session.get('cart', {})

    if size_or_flavour:
        del cart[item_id]['items_by_variant'][size_or_flavour]
        if not cart[item_id]['items_by_variant']:
            cart.pop(item_id)
        messages.success(request, f'Removed {size_or_flavour.title()}\
             {product.name} from your cart')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    messages.info(request, f'Removed {product.name} from your cart')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

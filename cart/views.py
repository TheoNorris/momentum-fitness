from django.shortcuts import render, redirect


def view_cart(request):
    """A view to return the shopping cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """"Add a quantity of the specified product to the cart"""

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
            else:
                cart[item_id]['items_by_variant'][size_or_flavour] = quantity
        else:
            cart[item_id] = {'items_by_variant': {size_or_flavour: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)

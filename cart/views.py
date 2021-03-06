from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """ A view that renders the cart. """
    
    cart = request.session.get('cart', {})
    
    print(cart)
    
    
    
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    
    
    return redirect(reverse('index'))

    
def adjust_cart(request, id):
    """ Adjust the quantity of the specified template to the specified amount."""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('index'))
    

def remove_item(request, id):
    """Set the quantity of the specific template to 0."""
    cart = request.session.get('cart', {})
    
    cart.pop(id)
    
    return redirect(reverse('view_cart'))
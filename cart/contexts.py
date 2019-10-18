from django.shortcuts import get_object_or_404
from store.models import Template

def cart_contents(request):
    
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    template_count = 0
    for id, quantity in cart.items():
        template = get_object_or_404(Template, pk=id)
        total += quantity * template.price
        template_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'template': template})
        
        return { 'cart_items': cart_items, 'total': total, 'template_count': template_count }
    
    return {}
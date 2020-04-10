from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm

from .models import Template

# Create your views here.
def base(request):
    """ Render base.html """
    
    return render(request, 'base.html')

def index(request):
    """ Render index.html """
    
    queryset =  Template.objects.all()
    
    context = {
        'object_list' : queryset,
        'title': 'List'
    }
    
    cart = request.session.get('cart', {})
    
    for i in cart:
        print(i)
    
    return render(request, 'template_page.html', context, cart)
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = RegisterForm()
    
    return render(request, 'registration/registration.html', {'form': RegisterForm()})
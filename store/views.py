from django.shortcuts import render

from .models import Template

# Create your views here.
def base(request):
    """ Render base.html """
    
    return render(request, 'base.html')

def index(request):
    """ Render index.html """
    
    queryset =  Template.objects.all()
    context = { 'object_list' : queryset,
                'title': 'List'
    }
    
    return render(request, 'template_page.html', context)
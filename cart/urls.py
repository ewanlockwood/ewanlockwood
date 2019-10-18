from django.urls import path, include

from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/?P<int:template_id>/', add_to_cart, name='add_to_cart'),
    path('adjust/?P<int:template_id>', adjust_cart, name='adjust_cart')
]

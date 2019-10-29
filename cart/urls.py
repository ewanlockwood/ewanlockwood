from django.urls import path, include

from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/?P<id>/d+', add_to_cart, name='add_to_cart'),
    path('adjust/<id>', adjust_cart, name='adjust_cart')
]

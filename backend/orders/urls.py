from django.urls import path
from .views import addOrderView, orderUpdateView, orderlistView, deleteOrderView

urlpatterns = [
    path('add-order/', addOrderView, name='add-order'),
    path('add-order/<int:id>/', orderUpdateView, name='order-update'),
    path('order-list/', orderlistView, name='order-list'),
    path('delete-order/<int:id>/', deleteOrderView, name='delete-order')

]
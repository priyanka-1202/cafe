from django.urls import path
from order.views import order

urlpatterns = [
    path('order/<int:table_no>/<str:item>/', order, name='order'),
]
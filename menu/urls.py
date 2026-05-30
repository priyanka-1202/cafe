from django.urls import path
from menu.views import home, menu, food

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('food/<int:id>/', food, name='food')
]
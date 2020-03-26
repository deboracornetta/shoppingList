from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('add', views.addNewItem, name='add'),
        path('bought/<item_id>', views.boughtItem, name='bought'),
        path('delete', views.deleteBought, name='deleteBought'),
        path('delete/<item_id>', views.deleteItem, name='deleteItem'),
]
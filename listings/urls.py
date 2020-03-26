from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_new_item, name="add"),
    path("bought/<item_id>", views.bought_item, name="bought"),
    path("delete/all", views.delete_all, name="delete_all_items"),
    path("delete/bought", views.delete_items_bought, name="delete_items_bought"),
    path("delete/<item_id>", views.delete_item, name="delete_item"),
]

app_name = "listings"

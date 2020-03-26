from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import ListingForm
from .models import ShoppingList


def index(request):
    new_item = ShoppingList.objects.order_by("id")
    form = ListingForm()
    context = {"new_item": new_item, "form": form}
    return render(request, "listings/index.html", context)


@require_POST
def add_new_item(request):
    form = ListingForm(request.POST)

    if form.is_valid():
        messages.success(request, "New item added!")
        my_new_item = ShoppingList(item_to_buy=request.POST["text"])
        my_new_item.save()

    return redirect("listings:index")


def bought_item(request, item_id):
    myItem = ShoppingList.objects.get(pk=item_id)
    myItem.bought = not myItem.bought
    myItem.save()

    messages.success(request, "Item updated")
    return redirect("listings:index")


def delete_all(request):
    ShoppingList.objects.filter().delete()

    messages.warning(request, "All items deleted!")
    return redirect("listings:index")


def delete_items_bought(request):
    ShoppingList.objects.filter(bought__exact=True).delete()

    messages.warning(request, "All bought items deleted!")
    return redirect("listings:index")


def delete_item(request, item_id):
    newItem = ShoppingList.objects.filter(pk=item_id).first()
    if not newItem:
        messages.error(request, "Item not found!")
        return redirect("listings:index")

    newItem.delete()
    messages.warning(request, "Item deleted!")
    return redirect("listings:index")

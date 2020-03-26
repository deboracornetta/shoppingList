from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import ListingForm
from .models import ShoppingList


def index(request):
    new_item = ShoppingList.objects.order_by('id')
    form = ListingForm()
    context = {'new_item': new_item, 'form': form}
    return render(request, 'listings/index.html', context)


@require_POST
def addNewItem(request):
    form = ListingForm(request.POST)

    if form.is_valid():
        my_new_item = ShoppingList(item_to_buy=request.POST['text'])
        my_new_item.save()
    
    return redirect('index')

def boughtItem(request, item_id):
    myItem = ShoppingList.objects.get(pk=item_id)
    myItem.bought = not myItem.bought
    myItem.save()

    return redirect('index')

def deleteBought(request):
    ShoppingList.objects.filter(bought__exact=True).delete()
    return redirect('index')

def deleteItem(request, item_id):
    newItem = ShoppingList.objects.get(pk=item_id)
    newItem.delete()
    return redirect('index')

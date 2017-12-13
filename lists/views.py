from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import WishList, Event, Items


def index(request):
    owner = request.user
    context = {'owner': owner}
    if owner == None:
        return render(request, 'lists/index.html')
    return render(request, 'lists/index.html', context)

def wishlist(request, owner_id):
    newest_list = WishList.objects.filter(owner = owner_id).order_by('-date_added')
    context = {'newest_list': newest_list,}
    return render(request, 'lists/wishlist.html', context)

def list_detail(request, wishlist_id):
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    event = Event.objects.get(wishlist=wishlist_id)
    items = Items.objects.filter(wishlist=wishlist_id)
    context = {'wishlist': wishlist, 'event': event, 'items': items}
    return render(request, 'lists/itemlist.html', context)

def item_detail(request, item_id):
    item = Items.objects.get(id=item_id)
    context = {'item': item}
    return render(request, 'lists/itemdetail.html', context)

from django.shortcuts import render, get_object_or_404

from .models import WishList, Event, Items

def index(request):
    newest_list = WishList.objects.order_by('-date_added')
    context = {'newest_list': newest_list,}
    return render(request, 'lists/index.html', context)

def list_detail(request, wishlist_id):
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    event = Event.objects.get(wishlist=wishlist_id)
    items = Items.objects.filter(wishlist=wishlist_id)
    context = {'wishlist': wishlist, 'event': event, 'items': items}
    return render(request, 'lists/wishlist.html', context)

def item_detail(request, item_id):
    item = Items.objects.get(id=item_id)
    context = {'item': item}
    return render(request, 'lists/item.html', context)

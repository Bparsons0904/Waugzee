from django.contrib import admin

from .models import WishList, Event, Items

admin.site.register(WishList)
admin.site.register(Event)
admin.site.register(Items)

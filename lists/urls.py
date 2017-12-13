from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/<int:owner_id>/', views.wishlist, name='wishlist'),
    path('itemlist/<int:wishlist_id>/', views.list_detail, name='itemlist'),
    path('item/<int:item_id>/', views.item_detail, name='itemdetail'),
]

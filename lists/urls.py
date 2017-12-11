from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/<int:wishlist_id>/', views.list_detail, name='wishlist'),
    path('item/<int:item_id>/', views.item_detail, name='item'),
]

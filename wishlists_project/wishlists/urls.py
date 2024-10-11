from django.urls import path
from . import views

app_name = 'wishlists'

urlpatterns = [
    path('', views.wishlist_item_list, name='wishlist_item_list'),
    path('create/', views.wishlist_item_create, name='wishlist_item_create'),
    path('update/<int:pk>/', views.wishlist_item_update, name='wishlist_item_update'),
    path('delete/<int:pk>/', views.wishlist_item_delete, name='wishlist_item_delete'),
    path('user/<str:username>/', views.wishlist_item_detail, name='wishlist_item_detail'),
]

from django.contrib import admin
from django.urls import path

from AppTerceraPreEntrega.views import *

urlpatterns = [
    #Url Client
    path('client/', ClientsListView.as_view(), name='list_clients'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="view_client"),
    path('client_form/', ClientCreateView.as_view(), name="create_client"),
    path('edit-client/<int:pk>/', ClientUpdateView.as_view(), name="edit_client"),
    path('delete-client/<int:pk>/', ClientDeleteView.as_view(), name="delete_client"),
    #Url Seller
    path('seller/', SellerListView.as_view(), name='list_sellers'),
    path('seller/<int:pk>/', SellerDetailView.as_view(), name="view_seller"),
    path('seller_form/', SellerCreateView.as_view(), name="create_seller"),
    path('edit-seller/<int:pk>/', SellerUpdateView.as_view(), name="edit_seller"),
    path('delete-seller/<int:pk>/', SellerDeleteView.as_view(), name="delete_seller"),
    path("search-seller/", search_seller, name="search_seller"),
    #Url Product
    path('product/', ProductListView.as_view(), name='list_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="view_product"),
    path('product_form/', ProductCreateView.as_view(), name="create_product"),
    path('edit-product/<int:pk>/', ProductUpdateView.as_view(), name="edit_product"),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name="delete_product"),
    #Url Sale
    path('sale/', SaleListView.as_view(), name='list_sales'),
    path('sale/<int:pk>/', SaleDetailView.as_view(), name="view_sale"),
    path('sale_form/', SaleCreateView.as_view(), name="create_sale"),
    path('delete-sale/<int:pk>/', SaleDeleteView.as_view(), name="delete_sale"),

]
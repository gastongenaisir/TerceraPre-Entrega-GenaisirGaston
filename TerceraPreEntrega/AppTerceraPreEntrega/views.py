from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from AppTerceraPreEntrega.models import Client, Seller, Product, Sale

def searchSale(request):

    return render(request, "")

def search(request):
    respuesta = f"La venta solicitada es:"

def search_seller(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        resultado = Seller.objects.filter(username__contains=busqueda)
        contexto = {
            "object_list": resultado,
        }
        http_response = render(
            request=request,
            template_name='list_sellers.html',
            context=contexto,
        )
        return http_response

##*****************************
##*****   Views Clients   *****
##*****************************
class ClientsListView(ListView):
    model = Client
    template_name = 'list_clients.html'
    
class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'phone')
    success_url = reverse_lazy('list_clients')


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy('list_clients')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'phone')
    success_url = reverse_lazy('list_clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('list_clients')


##*****************************
##*****   Views Sellers   *****
##*****************************
class SellerListView(ListView):
    model = Seller
    template_name = 'list_sellers.html'
    
class SellerCreateView(CreateView):
    model = Seller
    fields = ('username', 'first_name', 'last_name', 'email', 'phone','birthday_day')
    success_url = reverse_lazy('list_sellers')


class SellerDetailView(DetailView):
    model = Seller
    success_url = reverse_lazy('list_sellers')


class SellerUpdateView(UpdateView):
    model = Seller
    fields = ('first_name', 'last_name', 'email', 'phone','birthday_day')
    success_url = reverse_lazy('list_sellers')


class SellerDeleteView(DeleteView):
    model = Seller
    success_url = reverse_lazy('list_sellers')


##*****************************
##*****   Views Product   *****
##*****************************
class ProductListView(ListView):
    model = Product
    template_name = 'list_products.html'
    
class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'brand', 'price', 'stock')
    success_url = reverse_lazy('list_products')


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('list_products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'brand', 'price', 'stock')
    success_url = reverse_lazy('list_products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list_products')

##***************************
##*****   Views Sales   *****
##***************************
class SaleListView(ListView):
    model = Sale
    template_name = 'list_sales.html'
    
class SaleCreateView(CreateView):
    model = Sale
    fields = ('username', 'client', 'product', 'amount', 'total_price')
    success_url = reverse_lazy('list_sales')


class SaleDetailView(DetailView):
    model = Sale
    success_url = reverse_lazy('list_sales')

class SaleDeleteView(DeleteView):
    model = Sale
    success_url = reverse_lazy('list_sales')
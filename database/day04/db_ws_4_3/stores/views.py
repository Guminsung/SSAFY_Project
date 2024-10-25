import re
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from stores.forms import ProductForm, StoreForm
from .models import Store

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_form = ProductForm()
    products = store.product_set.all()
    context = {
        'store': store,
        'product_form':product_form,
        'products':products,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form':form
    }
    return render(request, 'stores/create.html', context)

def create_product(request, store_pk):
    store = Store.objects.get(pk = store_pk)
    product_form = ProductForm(request.POST)
    if product_form.is_valid():
        product = product_form.save(commit=False)
        product.user = request.user
        product.store = store
        product_form.save()
        return redirect('stores:detail', store_pk=store.pk)
    context = {
        'store':store,
        'product_form':product_form,
    }
    return render(request, 'stores/detail.html', context)

from django.shortcuts import render
from .models import Product, Category

def product_list(req):
    context = {
        'products': Product.objects.all()
    }
    return render(req, 'catalog/product_list.html', context)

def category(req, slug=None):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'products': Product.objects.filter(category=category)
    }
    return render(req, 'catalog/category.html', context)

def product(req, slug=None):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(req, 'catalog/product.html', context)

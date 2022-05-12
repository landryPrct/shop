
from django.utils  import timezone
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView
from .models import Product,Category


def product_detail(request,category_slug,slug):
    products=get_object_or_404(Product,slug=slug)

    context={'product': products}
    return  render(request,'category_detail.html',context)

def category_detail(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=category.products.all()
    context={'categories':category,'products': products}
    return  render(request,'category_detail.html',context)







    
   


    
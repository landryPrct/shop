from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from apps.store.models import Product


class Frontpage(ListView):
    model=Product
    context_object_name ='products'
    template_name= 'frontpage.html'

class Contact(TemplateView):
    template_name='contact.html'
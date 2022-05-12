


from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Frontpage(TemplateView):
    template_name= 'frontpage.html'

class Contact(TemplateView):
    template_name='contact.html'
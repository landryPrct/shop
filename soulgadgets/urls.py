
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Frontpage.as_view(),name='frontpage'),
path('contact',views.Contact.as_view(),name='contact'),
]

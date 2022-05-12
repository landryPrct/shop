
from django.contrib import admin
from django.urls import path
from apps.core import views
from apps.store import views as views_store

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Frontpage.as_view(), name='frontpage'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('<slug:category_slug>/<slug:slug>',
         views_store.product_detail, name='product_detail'),
     path('<slug:slug>',
         views_store.category_detail, name='category_detail'),

]

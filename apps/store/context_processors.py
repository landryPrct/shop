
from .models import Category


def menu_categories(request):
    category = Category.objects.all()
    return {'menu_categories':category}
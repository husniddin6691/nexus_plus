from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category, Region
from product.models import Product, ProductImage


def main(request):
    categories = Category.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    print(products),
    regions = Region.objects.all()
    ctx = {
        "categories": categories,
        "products": products,
        "regions": regions
    }
    return render(request, 'index.html', ctx)

def services_page(request):
    ctx = {}
    return render(request, 'services.html', ctx)



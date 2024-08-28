from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

def catalog(request, category_slug, page=1):
    
    if category_slug == 'all':
        goods = Products.objects.all()
    else:        
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, 2)
    current_page = paginator.page(page)

    context = {
        
        'title': 'Райський сад - Каталог товарів',
        'goods': current_page,
        'slug_url': category_slug,
        
    }
  
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'title': f'Райський сад - {product.name}',
        'product': product,
        
    }
  
    return render(request, 'goods/product.html', context)
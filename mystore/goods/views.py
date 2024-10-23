from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
from .utils import q_search

def catalog(request, category_slug = None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)  # Get the current page number or default to 1 if not provided in the URL query string.
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:        
        goods = Products.objects.filter(category__slug=category_slug)


    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 2)
    current_page = paginator.page(int(page))

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
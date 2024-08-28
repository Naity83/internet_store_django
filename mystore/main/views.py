from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories


def index(request):
    
    context = {
        'title': 'Райський сад - Садженці',
        'content': 'Райський Сад',
        
       
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Райський сад - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Пишемо про наш магазин',

    }
    return render(request, 'main/about.html', context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }

    return render(request, 'index.html', context)


def item(request):
    return HttpResponse('Item')


def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }

    return render(request, 'detail.html', context)

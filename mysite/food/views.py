from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
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


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'item_form.html', {'form': form})


def edit(request, pk):
    item = Item.objects.get(pk=pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'item_form.html', {'form': form, 'item': item})


def delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'item_delete.html', {'item': item})

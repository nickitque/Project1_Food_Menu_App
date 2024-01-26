from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }

    return render(request, 'index.html', context)


class IndexClassView(ListView):
    """Class based view instead of old view."""
    model = Item
    template_name = 'index.html'
    context_object_name = 'item_list'


def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }

    return render(request, 'detail.html', context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'item_form.html', {'form': form})


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_descr', 'price', 'item_img']
    template_name = 'item_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



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

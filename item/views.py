from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Catagory
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('catagory', 0)  
    categories = Catagory.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/item.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id) 
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item.pk)[:4]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:item_detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })

@login_required
def new(request):
   if request.method == 'POST':
         form = NewItemForm(request.POST, request.FILES)

         if form.is_valid():
              new_item = form.save(commit=False)
              new_item.created_by = request.user
              new_item.save()
              return redirect('item:item_detail', pk=new_item.pk)
         else:
             form = NewItemForm()



   form = NewItemForm(request.POST or None, request.FILES or None)

   return render(request, 'item/form.html', {
       'form': form,
       'title': 'New Item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashbord:index')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ContactForm  # Если вы ещё не создали forms.py, временно удалите эту строку и функцию contact ниже

def home(request):
    items = Item.objects.filter(is_active=True)
    return render(request, 'landing/home.html', {'items': items})

def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'landing/detail.html', {'item': item})

# Эта функция нужна, если вы делаете форму обратной связи
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) 
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'landing/contact.html', {'form': form})
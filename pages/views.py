from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Sneakers
from .forms import SneakersForm, BrandForm
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        form = BrandForm(request.POST or None)

        if form.is_valid():
            form.save()
            return render(request, 'pages/index.html')
    else:
        sneakers = Sneakers.objects.order_by('-id')
        context = {
            'sneakers' : sneakers
        }
        return render(request, 'pages/index.html', context)


def add_sneakers(request):
    if request.method == 'POST':
        form = SneakersForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = SneakersForm()
        return render(request, 'pages/add_model.html', {'form' : form})


def sneakers_details(request, pk):
    sneakers_id = get_object_or_404(Sneakers, pk=pk)
    context = {
        'sneakers_id' : sneakers_id
    }
    return render(request, 'pages/sneaker_details.html', context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .models import Sneakers
from .forms import SneakersForm, BrandForm
from django.urls import reverse
from django.contrib import messages


def index(request):
    query = request.GET.get('q')
    if query:
        sneakers = Sneakers.objects.filter(model_name__icontains=query)
        return render(request, 'pages/index.html', {'sneakers' : sneakers})
    else:
        sneakers = Sneakers.objects.order_by('-id')
        context = {
            'sneakers' : sneakers
        }
        return render(request, 'pages/index.html', context)


def add_sneakers(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SneakersForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(index))
        else:
            form = SneakersForm()
            return render(request, 'pages/add_model.html', {'form' : form})
    else:
        return render(request, 'pages/add_model.html')

def sneakers_details(request, pk):
    sneakers_id = get_object_or_404(Sneakers, pk=pk)
    context = {
        'sneakers_id' : sneakers_id
    }
    return render(request, 'pages/sneaker_details.html', context)


def delete_sneakers(request, pk):
    sneakers = Sneakers.objects.get(pk=pk)
    sneakers.delete()
    return HttpResponseRedirect(reverse(index))


def edit_sneakers(request, pk):
    sneakers = get_object_or_404(Sneakers, pk=pk)

    if request.method == 'POST':
        form = SneakersForm(request.POST, instance=sneakers)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your sneakers has been updated!')
        except Exception as e:
            messages.warning(request, 'Your sneakers werent updated due to error{}'.format(e))

    else:
        form = SneakersForm(instance=sneakers)
    return render(request,'pages/edit_sneakers.html', {'form' : form,
                                                       'sneakers' : sneakers})
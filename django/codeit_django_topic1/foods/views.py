from datetime import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render

from foods.models import Menu

# Create your views here.
# FBV

def index(request):
    today = datetime.today()
    menus = Menu.objects.all()

    context = dict()
    context["date"] = today
    context["menus"] = menus

    return render(request, 'foods/index.html', context=context)


# def chicken(request):
#     return render(request, 'foods/chicken.html')


def food_detail(request, pk):
    menu = Menu.objects.get(pk=pk)

    context = dict()
    context["menu"] = menu

    return render(request, 'foods/detail.html', context=context)
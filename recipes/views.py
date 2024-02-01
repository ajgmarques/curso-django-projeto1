from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jana',
    })


def contato(request):
    return HttpResponse('**** CONTATO ****')
    # return HTTP responde


def sobre(request):
    return HttpResponse('**** SOBRE ****')
    # return HTTP responde

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('**** HOME ****')
    # return HTTP responde


def contato(request):
    return HttpResponse('**** CONTATO ****')
    # return HTTP responde


def sobre(request):
    return HttpResponse('**** SOBRE ****')
    # return HTTP responde

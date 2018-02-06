from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You made it to the fricking #web")


def secret():
    return HttpResponse("OH FUCk swild")


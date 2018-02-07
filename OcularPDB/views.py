from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "ocular_proteome_db/home.html")


# def secret(name):
#     return HttpResponse("OH FUCk swild"+name)


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def results(request):
    return HttpResponse("OH FUCk swild")
    #return render(request, "ocular_proteome_db/results.html")


def index(request):
    return render(request, "ocular_proteome_db/results.html")




# def secret(name):
#     return HttpResponse("OH FUCk swild"+name)


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def results(request):
    return HttpResponse("Flowers and blue sky!")#replace this line with line below
    #return render(request, "ocular_proteome_db/results.html")


def index(request):
    return render(request, "ocular_proteome_db/results.html")





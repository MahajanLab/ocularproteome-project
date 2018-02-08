from django.shortcuts import render


def results(request):
    return render(request, "ocular_proteome_db/results.html")


def index(request):
    return render(request, "ocular_proteome_db/home.html")

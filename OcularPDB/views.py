from django.shortcuts import render
from OcularPDB.models import RetinaProtein


def results(request):
    identifier = request._post['identifier']
    proteins = RetinaProtein.objects.get(pk=identifier)
    vars = {'proteins': proteins}

    return render(request, "ocular_proteome_db/results.html", context=vars)


def index(request):
    return render(request, "ocular_proteome_db/home.html")


def download(request):
    return render(request, "ocular_proteome_db/download.html")

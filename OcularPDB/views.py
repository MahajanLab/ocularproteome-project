from django.shortcuts import render
from OcularPDB.models import RetinaProtein


def results(request):
    identifier = request._post['identifier']

    proteinS = identifier.split(', ')
    errorProteins = []

    for p in range(len(proteinS)):
        try:
            protein = RetinaProtein.objects.get(pk=p)
            vars = {'protein': protein}
            return render(request, "ocular_proteome_db/results.html", context=vars)
        except:
            errorProteins.append(p)
            return render(request, "ocular_proteome_db/results.html", context = "Errorsx")


def index(request):
    return render(request, "ocular_proteome_db/home.html")


def download(request):
    return render(request, "ocular_proteome_db/download.html")

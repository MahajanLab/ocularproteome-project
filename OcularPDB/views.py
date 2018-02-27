from django.shortcuts import render
from OcularPDB.models import RetinaProtein


def results(request):
    identifier = request._post['identifier']

    protein_array = identifier.split(' ')  # split elements in input into different elements at a space
    error_proteins = []  # list to store proteins entered but not found in database

    print(protein_array[0])
    protein = RetinaProtein.objects.get(pk=protein_array[0])  # return a RetinaProtein object
    protein_list = [protein]  # add the RetinaProtein object to list which will hold all the proteins

    for i in range(1, len(protein_array)):
        try:
            protein = RetinaProtein.objects.get(pk=protein_array[i])  # get next Protein object
            protein_list.append(protein)  # append new protein to list
        except:
            print("error", protein_array[i])
            error_proteins.append(protein_array[i] + ' ')  # if the protein is not found in the database, add it to the list

    data = {'protein_list': protein_list,
            'error_list': error_proteins}

    return render(request, "ocular_proteome_db/results.html", context=data)


def index(request):
    return render(request, "ocular_proteome_db/home.html")


def download(request):
    return render(request, "ocular_proteome_db/download.html")

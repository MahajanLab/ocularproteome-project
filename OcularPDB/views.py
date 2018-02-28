from django.shortcuts import render
from OcularPDB.models import RetinaProtein
from OcularPDB.models import ChoroidProtein


def results(request):
    identifier = request._post['identifier']

    protein_input = identifier.split(' ')  # split elements in input into different elements at a space
    error_proteins = []  # list to store proteins entered but not found in database
    protein_list = []  # add the RetinaProtein object to list which will hold all the proteins

    for i in range(len(protein_input)):
        p_found, p_error = RetinaProtein.search(protein_input[i])
        if p_found is None:
            error_proteins.append(p_error + ' ')  # if the protein is not found in the database, add it to the list
        else:
            protein_list.append(p_found)  # append new protein to list

        p_found, p_error = ChoroidProtein.search(protein_input[i])
        if p_found is None:
            error_proteins.append(p_error + ' ')  # if the protein is not found in the database, add it to the list
        else:
            protein_list.append(p_found)  # append new protein to list
            


    data = {'protein_list': protein_list,
            'error_list': error_proteins}

    return render(request, "ocular_proteome_db/results.html", context=data)




def index(request):
    return render(request, "ocular_proteome_db/home.html")


def download(request):
    return render(request, "ocular_proteome_db/download.html")

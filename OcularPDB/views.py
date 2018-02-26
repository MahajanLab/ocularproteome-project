from django.shortcuts import render
from OcularPDB.models import RetinaProtein


def results(request):
    identifier = request._post['identifier']

    protein_array = identifier.split(' ')  # split elements in input into different elements at a space
    error_proteins = []  # list to store proteins entered but not found in database

    print(protein_array[0])
    protein = RetinaProtein.objects.get(pk=protein_array[0])  # return a RetinaProtein object
    protein_dict = {protein_array[0]: protein}  # add the RetinaProtein object to dict which will hold all the proteins

    for i in range(1, len(protein_array)):
        try:
            protein = RetinaProtein.objects.get(pk=protein_array[i])  # return a RetinaProtein object
            dict_el = {protein_array[i]: protein}  # add RetinaProtein object to a dict object
            print(dict_el)
            protein_dict.update(dict_el)  # update dict with dict object containing the last protein
        except:
            print("error", protein_array[i])
            error_proteins.append(protein_array[i])  # if the protein is not found in the database, add it to the list

    return render(request, "ocular_proteome_db/results.html", context=protein_dict)


def index(request):
    return render(request, "ocular_proteome_db/home.html")

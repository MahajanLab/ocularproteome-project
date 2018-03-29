from django.shortcuts import render
from django.http import HttpResponse
from OcularPDB.models import RetinaProtein, ChoroidProtein, VitreousProtein, MouseRetina, MouseVitreous
import re


def results(request):
    identifier = request._post['identifier']
    protein_input = list(set(re.findall('[a-zA-Z0-9_-]+', identifier)))  # split elements in input into different elements at a space

    error_proteins = []  # list to store proteins entered but not found in database
    human_retina_rpe = []  # add the RetinaProtein object to list which will hold all the proteins
    mouse_proteins = []
    human_vitreous = []


    protein_list_strings = []

    error_proteins.clear()

    for i in range(len(protein_input)):
        found = False

        # Search in Retina table
        retina_protein = RetinaProtein.search(protein_input[i])
        if retina_protein is not None:
            found = True
            human_retina_rpe.append(retina_protein)
            protein_list_strings.append(retina_protein.ens_id + ' ')

        # Search in RPE-Choroid table
        choroid_protein = ChoroidProtein.search(protein_input[i])
        if choroid_protein is not None:
            found = True
            human_retina_rpe.append(choroid_protein)
            protein_list_strings.append(choroid_protein.ens_id + ' ')

        # Search in Vitreous table
        vitreous_protein = VitreousProtein.search(protein_input[i])
        if vitreous_protein is not None:
            found = True
            human_vitreous.append(vitreous_protein)
            protein_list_strings.append(vitreous_protein.ens_id + ' ')

        # Search mouse table
        mouse_retina_protein = MouseRetina.search(protein_input[i])
        if mouse_retina_protein is not None:
            found = True
            mouse_proteins.append(mouse_retina_protein)
            protein_list_strings.append(mouse_retina_protein)

        # Search mouse table
        mouse_vitreous_protein = MouseVitreous.search(protein_input[i])
        if mouse_vitreous_protein is not None:
            found = True
            mouse_proteins.append(mouse_vitreous_protein)
            protein_list_strings.append(mouse_vitreous_protein)

        if not found:
            error_proteins.append(protein_input[i] + ' ')

    error_proteins = list(set(error_proteins))
    print(protein_list_strings)
    error_proteins = list(set(error_proteins)-set(protein_list_strings))

    data = {'human_vitreous': human_vitreous,
            'human_retina_rpe': human_retina_rpe,
            'mouse_proteins': mouse_proteins,
            'error_list': error_proteins,
            'search_text': identifier}

    return render(request, "ocular_proteome_db/results.html", context=data)


def index(request):
    return render(request, "ocular_proteome_db/home.html")


def download(request):
    return render(request, "ocular_proteome_db/download.html")


zip_root_dir = "OcularPDB/static/"


def download_retina(request):
    with open(zip_root_dir + "Human_Retina_MahajanLab.xlsx", 'rb') as zipfile:
        response = HttpResponse(zipfile.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=Human_Retina_MahajanLab.xlsx'
        return response


def download_choroid(request):
    with open(zip_root_dir + "RPE_Choroid_MahajanLab.xlsx", 'rb') as zipfile:
        response = HttpResponse(zipfile.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=RPE_Choroid_MahajanLab.xlsx'
        return response


def download_vitreous(request):
    with open(zip_root_dir + "Human_Vitreous_MahajanLab.xlsx", 'rb') as zipfile:
        response = HttpResponse(zipfile.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=Human_Vitreous_MahajanLab.xlsx'
        return response

def download_mouse_vitrous(request):
    with open(zip_root_dir + "Mouse_Vitreous_MahajanLab.xlsx", 'rb') as zipfile:
        response = HttpResponse(zipfile.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=Mouse_Vitreous_MahajanLab.xlsx'
        return response

def download_mouse_retina(request):
    with open(zip_root_dir + "Mouse_Retina_MahajanLab.xlsx", 'rb') as zipfile:
        response = HttpResponse(zipfile.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=Mouse_Retina_MahajanLab.xlsx'
        return response



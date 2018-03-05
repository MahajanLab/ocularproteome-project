from django.db import models


# all proteins have an ensembl ID
# I think this is a good way to do things because then when we
# search for a protein by its ens_id, we only have to look in one place
# rather than having to search each model until we find it
# class Protein(models.Model):
#     ens_id = models.CharField(primary_key=True, max_length=200, default=0)
#
#
# # inherits from base class called Protein
# class RCProtein(Protein):
#     name = models.CharField(unique=True, max_length=200)
#     fovea_avg = models.IntegerField()
#     macula_avg = models.IntegerField()
#     periphery_avg = models.IntegerField()
#
#
# # inherits from base class called Protein
# class VProtein(Protein):
#     post_hyaloid_avg = models.IntegerField()
#     ant_hyaloid_avg = models.IntegerField()
#     vit_base_avg = models.IntegerField()
#     vit_core_avg = models.IntegerField()


class RetinaProtein(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(unique=True, max_length=255)
    data_set = 'Retina'
    fovea_avg = models.IntegerField()
    macula_avg = models.IntegerField()
    periphery_avg = models.IntegerField()

    # def __eq__(self, other):
    #     if(self.ens_id == other.)

    @staticmethod
    def search(protein_identifier):
        protein_error = None
        protein_found = None
        try:
            protein_found = RetinaProtein.objects.get(pk=protein_identifier)  # get next Protein object
        except:
            protein_error = protein_identifier

        if protein_found is None:
            try:
                protein_found = RetinaProtein.objects.filter(name=protein_identifier)[0]
            except IndexError:
                protein_error = protein_identifier

        return protein_found, protein_error

    def __str__(self):
        return self.ens_id


class ChoroidProtein(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(unique=True, max_length=255)
    data_set = 'Choroid'
    fovea_avg = models.IntegerField()
    macula_avg = models.IntegerField()
    periphery_avg = models.IntegerField()

    @staticmethod
    def search(protein_identifier):
        protein_error = None
        protein_found = None
        try:
            protein_found = ChoroidProtein.objects.get(pk=protein_identifier)  # get next Protein object
        except:
            protein_error = protein_identifier
            print("error", protein_identifier)

        if protein_found is None:
            try:
                protein_found = ChoroidProtein.objects.filter(name=protein_identifier)[0]
            except IndexError:
                protein_error = protein_identifier

        return protein_found, protein_error

    def __str__(self):
        return self.ens_id

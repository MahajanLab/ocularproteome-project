from django.db import models


# all proteins have an ensembl ID
# I think this is a good way to do things because then when we
# search for a protein by its ens_id, we only have to look in one place
# rather than having to search each model until we find it
class Protein(models.Model):
    ens_id = models.CharField(primary_key=True)


# inherits from base class called Protein
class RCProtein(Protein):
    name = models.CharField(unique=True)
    fovea_avg = models.IntegerField
    macula_avg = models.IntegerField
    periphery_avg = models.IntegerField


# inherits from base class called Protein
class VProtein(Protein):
    post_hyaloid_avg = models.IntegerField
    ant_hyaloid_avg = models.IntegerField
    vit_base_avg = models.IntegerField
    vit_core_avg = models.IntegerField

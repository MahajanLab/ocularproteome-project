from django.db import models


class RetinaProtein(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(max_length=255, null=True)
    tissue = 'Retina'
    fovea_avg = models.IntegerField()
    macula_avg = models.IntegerField()
    periphery_avg = models.IntegerField()

    # def __eq__(self, other):
    #     if(self.ens_id == other.)

    @staticmethod
    def search(protein_identifier):
        protein = None
        ens_results = RetinaProtein.objects.filter(ens_id=protein_identifier)
        name_results = RetinaProtein.objects.filter(name=protein_identifier)

        if ens_results.count() == 1:
            protein = ens_results.get()
        elif name_results.count() == 1:
            protein = name_results.get()

        return protein

    def __str__(self):
        return self.ens_id


class ChoroidProtein(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(max_length=255, null=True)
    tissue = 'RPE-Choroid'
    fovea_avg = models.IntegerField()
    macula_avg = models.IntegerField()
    periphery_avg = models.IntegerField()

    @staticmethod
    def search(protein_identifier):
        protein = None
        ens_results = ChoroidProtein.objects.filter(ens_id=protein_identifier)
        name_results = ChoroidProtein.objects.filter(name=protein_identifier)

        if ens_results.count() == 1:
            protein = ens_results.get()
        elif name_results.count() == 1:
            protein = name_results.get()

        return protein

    def __str__(self):
        return self.ens_id


class VitreousProtein(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(max_length=255, null=True)
    tissue = 'Vitreous'
    posterior_hyaloid = models.IntegerField()
    anterior_hyaloid = models.IntegerField()
    vitreous_base = models.IntegerField()
    vitreous_core = models.IntegerField()

    @staticmethod
    def search(protein_identifier):
        protein = None
        ens_results = VitreousProtein.objects.filter(ens_id=protein_identifier)
        name_results = VitreousProtein.objects.filter(name=protein_identifier)

        if ens_results.count() == 1:
            protein = ens_results.get()
        elif name_results.count() == 1:
            protein = name_results.get()

        return protein


class MouseRetina(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(max_length=255, null=True)
    tissue = 'Retina'
    count = models.IntegerField()

    @staticmethod
    def search(protein_identifier):
        protein = None
        ens_results = MouseRetina.objects.filter(ens_id=protein_identifier)
        name_results = MouseRetina.objects.filter(name=protein_identifier)

        if ens_results.count() == 1:
            protein = ens_results.get()
        elif name_results.count() == 1:
            protein = name_results.get()

        return protein


class MouseVitreous(models.Model):
    ens_id = models.CharField(primary_key=True, max_length=255, default='x')
    name = models.CharField(max_length=255, null=True)
    tissue = 'Vitreous'
    count = models.IntegerField()

    @staticmethod
    def search(protein_identifier):
        protein = None
        ens_results = MouseVitreous.objects.filter(ens_id=protein_identifier)
        name_results = MouseVitreous.objects.filter(name=protein_identifier)

        if ens_results.count() == 1:
            protein = ens_results.get()
        elif name_results.count() == 1:
            protein = name_results.get()

        return protein

from django.db import models



class Vehicules(models.Model):

    COMPT = [
        ("H", "H"),
        ("KM", "KM"),
    ]

    nparc = models.CharField(max_length=20, blank=True, null=True)
    noptim = models.CharField(max_length=20, blank=True, null=True)
    immat = models.CharField(max_length=20, blank=True, null=True)
    nature = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    marque = models.CharField(max_length=50, blank=True, null=True)
    modele = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    energie = models.CharField(max_length=20, blank=True, null=True)
    puissance = models.CharField(max_length=15, blank=True, null=True)
    type_compt = models.CharField(max_length=10, choices=COMPT)
    annee_mes = models.CharField(max_length=20, blank=True, null=True)
    statut = models.CharField(max_length=20, blank=True, null=True)
    affectation = models.CharField(max_length=100, blank=True, null=True)
    site = models.CharField(max_length=20, blank=True, null=True)
    responsable_sabc = models.CharField(max_length=255, blank=True, null=True)
    alert_compt = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.noptim}_{self.nparc}_{self.immat}"



class Personnel(models.Model):

    nom = models.CharField(max_length=255, blank=True)
    prenom = models.CharField(max_length=255, blank=True)
    fonction = models.CharField(max_length=255, blank=True)
    site = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.fonction}"

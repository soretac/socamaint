from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
import uuid
from django.core import validators





class Clients(TenantMixin):

    id_enreg            = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    schema_name         = models.CharField(max_length=255, unique=True)                         # Nom de location de l'entreprise dans la BD                                 
    created_on          = models.DateField("Date Enregistrement", auto_now_add=True)                                     # Date de creation de la location de l'entreprise
    nom_ese             = models.CharField("Nom Entreprise", max_length=255, blank=False, unique=True)
    schema_sigle        = models.CharField("Sigle Entreprise", max_length=255, unique=True)
    nom_domaine         = models.CharField("Nom Domaine Entreprise", max_length=255, default='localhost', unique=True)
    description_ese     = models.TextField("Description Entreprise", null=True, blank=True, default="Faire une description")
    email               = models.EmailField("Email Entreprise", max_length=255, unique=True, validators=[validators.EmailValidator(message="Email invalide")])
    mobile              = models.CharField("N° Telephone", max_length=255, blank=False, null=True)
    ese_activate        = models.BooleanField("Activation Entreprise", default=False)
    auto_create_schema = True
    auto_drop_schema = True


    def save(self,*args, **kwargs):
        self.nom_ese = self.nom_ese.lower()
        self.schema_sigle = self.schema_sigle.lower()
        self.nom_domaine = self.nom_domaine.lower()
        self.email = self.email.lower()
        return super(Clients, self).save(*args, **kwargs)
    
    class Meta: 
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return "{} ({}) - {}".format(self.nom_ese, self.schema_sigle, self.ese_activate)


class Domain(DomainMixin):
    pass
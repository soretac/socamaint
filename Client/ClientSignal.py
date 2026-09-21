from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from Client.models import Clients, Domain
from Entreprise.EntrepriseSerializer import EseSerializer
from Entreprise.models import Eses


@receiver(post_save, sender=Clients)
def CreateTenant(sender, instance, created, **kwargs):
    if not created:
        dom = Domain.objects.filter(tenant_id = instance.id_enreg).first()
        dom.domain = instance.nom_domaine + ".localhost"
        dom.save()


    else: 
        domain = Domain()
        domaine = instance.nom_domaine + ".localhost"   # LE SOUS DOMAINE DE L'ENTREPRISE #
        domain.domain = domaine
        domain.tenant = instance     # domain.tenant = client
        domain.is_primary = True
        domain.save()

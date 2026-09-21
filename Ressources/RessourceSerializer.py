from rest_framework import serializers
from .models import Vehicules, Personnel



class VehiculeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Vehicules
      fields = ["id", "nparc", "noptim", "immat", "nature", "type", "marque", "modele", "serie", "energie", "puissance", "type_compt", "annee_mes", "statut", "affectation", "site", "responsable_sabc", "alert_compt"]



class ImportEnginSerializer(serializers.Serializer):
   file = serializers.FileField()


class PersonnelSerializer(serializers.ModelSerializer):
   class Meta:
      model = Personnel
      fields = ["nom", "prenom", "fonction", "site"]
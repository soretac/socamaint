from rest_framework import serializers
from .models import Clients


class ClientEseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clients
        fields = ['id_enreg', 'schema_name', 'created_on', 'nom_ese', 'schema_sigle', 'nom_domaine', 'description_ese', 'email', 'mobile']
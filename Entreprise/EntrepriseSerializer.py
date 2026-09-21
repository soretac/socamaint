from rest_framework import serializers
from .models import Eses, Validation

class EseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eses
        fields = ['schema_name', 'created_on', 'nom_ese', 'schema_sigle', 'nom_domaine', 'description_ese', 'email', 'mobile']



class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = ['schema_name', 'nom_ese']
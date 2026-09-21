from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Eses, Validation
from .EntrepriseSerializer import EseSerializer, ValidationSerializer
from django.shortcuts import get_object_or_404
from Client.models import Clients
from rest_framework.response import Response
from django_tenants.utils import tenant_context
from rest_framework import status



class AccueilEntreprises(ListAPIView):
    queryset = Eses.objects.all()
    serializer_class = EseSerializer

class Valid(CreateAPIView):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer 

    def post(self, request, *args, **kwargs):
        
        data = request.data
        nom_ese = data["nom_ese"].lower()
        schema_name = data["schema_name"].lower()
        erese = get_object_or_404(Clients, schema_name=schema_name)
        client = Clients.objects.filter(schema_name=schema_name).first()
        if erese != None:
            client.ese_activate=True
            client.save()
                
            data = {}
            
            with tenant_context(client):
                data["schema_name"] = client.schema_name
                data["created_on"] = client.created_on
                data["nom_ese"] = client.nom_ese
                data["schema_sigle"] = client.schema_sigle
                data["nom_domaine"] = client.nom_domaine
                data["description_ese"] = client.description_ese
                data["email"] = client.email
                data["mobile"] = client.mobile

                serializer = EseSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()


                return Response({'status': True, 'message': "Entreprise enregistrée avec succès et abonnement validé"}, status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Clients
from .ClientSerializer import ClientEseSerializer


class ClientViewSet(ModelViewSet):
    parser_classes = [FormParser, MultiPartParser]
    queryset = Clients.objects.all()
    serializer_class = ClientEseSerializer

from django.shortcuts import render
from rest_framework import viewsets

from main.models import Nota
from main.serializers import NotaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
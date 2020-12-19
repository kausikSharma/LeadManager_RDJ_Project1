from rest_framework import viewsets,permissions

from django.shortcuts import render
from leads.models import Lead
from leads.serializers import LeadSerializer 



class LeadViewSet(viewsets.ModelViewSet):
    queryset=Lead.objects.all()
    serializer_class=LeadSerializer
    permission_classes=[
        permissions.AllowAny
    ]
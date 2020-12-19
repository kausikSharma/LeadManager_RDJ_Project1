from rest_framework import serializers
from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """Lead serializer is used to create serializer"""
    class Meta:
        model=Lead
        fields="__all__"
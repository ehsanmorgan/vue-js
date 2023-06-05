from rest_framework import serializers
from .models import ToDo_List




class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo_List
        fields='__all__'
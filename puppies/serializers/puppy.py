from rest_framework import serializers
from ..models.puppy import Puppy

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'size','age', 'breed', 'color', 'created_at', 'updated_at')
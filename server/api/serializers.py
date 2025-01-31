# serializers.py
from rest_framework import serializers
from .models import Crop, Disease, Step


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['id', 'name', 'description', 'remedies']


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['step', 'title', 'details']


class CropSerializer(serializers.ModelSerializer):
    diseases = DiseaseSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Crop
        fields = ['id', 'name', 'soil_type', 'pH_range',
                  'growing_period', 'diseases', 'steps']

# views.py
from rest_framework import viewsets
from .models import Crop, Disease, Step
from .serializers import CropSerializer, DiseaseSerializer, StepSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.prefetch_related('diseases', 'steps').all()
    serializer_class = CropSerializer


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

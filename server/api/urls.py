# urls.py (app-level)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, DiseaseViewSet, StepViewSet ,PredictViewPotato,  PredictViewTomato 

router = DefaultRouter()
router.register(r'crops', CropViewSet, basename='crop')
router.register(r'diseases', DiseaseViewSet, basename='disease')
router.register(r'steps', StepViewSet, basename='step')

urlpatterns = [
    path('', include(router.urls)),
    path('potato/predict/', PredictViewPotato.as_view(), name='predict-disease-potato'),
    path('tomato/predict/', PredictViewTomato.as_view(), name='predict-disease-tomato'),
    
]

# Include this in your project's main urls.py like:
# path('api/', include('your_app.urls'))

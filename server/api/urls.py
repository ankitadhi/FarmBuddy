# urls.py (app-level)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, DiseaseViewSet, StepViewSet

router = DefaultRouter()
router.register(r'crops', CropViewSet, basename='crop')
router.register(r'diseases', DiseaseViewSet, basename='disease')
router.register(r'steps', StepViewSet, basename='step')

urlpatterns = [
    path('', include(router.urls)),
]

# Include this in your project's main urls.py like:
# path('api/', include('your_app.urls'))

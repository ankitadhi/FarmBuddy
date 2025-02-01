# views.py
import os
from rest_framework import viewsets, status
from .models import Crop, Disease, Step
from .serializers import CropSerializer, DiseaseSerializer, StepSerializer
import pickle
from rest_framework.views import APIView
import numpy as np
from rest_framework.response import Response
from PIL import Image



class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.prefetch_related('diseases', 'steps').all()
    serializer_class = CropSerializer


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class PredictViewPotato(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if 'image' not in request.FILES:
                return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

            # Load model
            model = self.load_model()

            # Preprocess image
            img = Image.open(request.FILES['image'])
            processed_img = self.preprocess_image(img)  # Correct method call

            # Make prediction
            prediction = model.predict(processed_img[np.newaxis, ...])
            class_idx = np.argmax(prediction, axis=1)[0]

            return Response({
                "prediction": self.class_mapping(class_idx)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Helper methods (must be INSIDE the class)
    def load_model(self):
        model_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '.', 'ml_models', 'potato.pkl')
        with open(model_path, 'rb') as f:
            return pickle.load(f)

    def preprocess_image(self, img):  # Correctly indented under the class
        img = img.convert('RGB')
        img = img.resize((256, 256))
        return np.array(img) / 255.0

    def class_mapping(self, class_idx):
        return ['Healthy', 'Early Blight', 'Late Blight'][class_idx]


class PredictViewTomato(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if 'image' not in request.FILES:
                return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

            # Load model
            model = self.load_model()

            # Preprocess image
            img = Image.open(request.FILES['image'])
            processed_img = self.preprocess_image(img)

            # Make prediction
            prediction = model.predict(processed_img)
            class_idx = np.argmax(prediction, axis=1)[0]

            return Response({
                "prediction": self.class_mapping(class_idx)
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def load_model(self):
        model_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), '.', 'ml_models', 'tomato.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print(f"Model input shape: {model.input_shape}")  # Debug
        return model

    def preprocess_image(self, img):
        # Convert image to RGB and resize to match model's expected input size (224x224)
        img = img.convert('RGB')
        img = img.resize((224, 224))  # Resize image to 224x224
        img_array = np.array(img) / 255.0  # Normalize pixel values to [0, 1]

        # Add batch dimension (1, 224, 224, 3)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def class_mapping(self, class_idx):
        # Map predicted class index to the corresponding class label
        return [
            "Bacterial Spot",
            "Early Blight",
            "Late Blight",
            "Leaf Mold",
            "Septoria Leaf Spot",
            "Spider Mites",
            "Target Spot",
            "Yellow Leaf Curl Virus",
            "Mosaic Virus",
            "Healthy"
        ][class_idx]

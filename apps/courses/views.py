from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Category

from .serializers import CategoryListSerializer

# Create your views here.

class CategoryListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer



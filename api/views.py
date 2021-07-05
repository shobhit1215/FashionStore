from django.shortcuts import render
from rest_framework import generics
from .models import Dress
from .serializers import DressSerializer
# Create your views here.
class DressList(generics.ListCreateAPIView):
    queryset = Dress.objects.all()
    serializer_class = DressSerializer

class DressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dress
    serializer_class = DressSerializer


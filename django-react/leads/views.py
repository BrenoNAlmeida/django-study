from django.shortcuts import render
from .serializers import LeadSerializer
from rest_framework import generics
from .models import Lead
# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
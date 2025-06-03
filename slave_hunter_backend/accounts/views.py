from django.shortcuts import render
from .serializers import CompanySerializer
from .models import Company
from rest_framework import viewsets
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly


# Create your views here.
# Company CRUD operations
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


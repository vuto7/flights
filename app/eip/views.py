from django.shortcuts import render
from .models import Employee, Identity, TimeStamp
from .serializers import EmployeeSerializer, IdentitySerializer, TimeStampSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters


class IdentityViewSet(viewsets.ModelViewSet):
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nrcid', 'lastname']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TimeStampViewSet(viewsets.ModelViewSet):
    queryset = TimeStamp.objects.all()
    serializer_class = TimeStampSerializer

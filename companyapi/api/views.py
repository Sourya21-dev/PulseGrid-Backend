from django.shortcuts import render

# Create your views here.
# VIEW OF MODEL COMPANY

from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):#This line defines a new viewset class called CompanyViewSet that inherits from the ModelViewSet class provided by Django REST Framework (DRF). A viewset is a class that defines the behavior of a set of views for a particular model. In this case, the CompanyViewSet will handle the views for the Company model.
    queryset = Company.objects.all()#This line defines the queryset for the CompanyViewSet. It specifies that the viewset should retrieve all instances of the Company model.
    serializer_class = CompanySerializer#This line defines the serializer class for the CompanyViewSet. It specifies that the viewset should use the CompanySerializer to convert Company model instances into JSON format and vice versa.


#Instead of manually writing functions to handle "Create", "Read", "Update", and "Delete" operations, 
#ModelViewSet automatically provides all of these capabilities. 
#It just needs to know which data to use (queryset = Company.objects.all()) and how to translate it (serializer_class = CompanySerializer).

#VIEW OF MODEL EMPLOYEE
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
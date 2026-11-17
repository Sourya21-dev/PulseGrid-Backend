from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):#This line defines a new serializer class called CompanySerializer that inherits from the HyperlinkedModelSerializer class provided by Django REST Framework (DRF).
    class Meta:#The Meta class is a nested class within the CompanySerializer class that provides metadata about the serializer. It is used to specify the model that the serializer is based on and the fields that should be included in the serialized representation.
        model = Company
        fields = "__all__"# This line specifies that all fields of the Company model should be included in the serialized representation. By using "__all__", DRF will automatically generate fields for each attribute of the Company model, including company_id, name, email, location, about, type, added_date, and active.

#By inheriting from HyperlinkedModelSerializer and setting fields = "__all__", 
#DRF automatically looks at the Company model and writes all the background translation logic to convert every column of that table into JSON format.


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
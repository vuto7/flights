from rest_framework import serializers
from .models import Employee, Identity, TimeStamp

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields='__all__'

class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields='__all__'

from rest_framework import serializers
from .models import *

class Studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields='__all__'
        
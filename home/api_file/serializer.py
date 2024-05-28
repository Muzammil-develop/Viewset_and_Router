from rest_framework import serializers
from home.models import Clinic

class ClinicSerializer (serializers.ModelSerializer):
    class Meta :
        model = Clinic
        fields = '__all__'
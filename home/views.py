from django.shortcuts import render
from home.models import Clinic
from home.api_file.serializer import ClinicSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class Clinic_view (viewsets.ViewSet):

    def list (self , request):
        query_set = Clinic.objects.all ()
        serializer = ClinicSerializer (query_set , many = True)
        return Response (serializer.data)
    
    def retrieve (self , request , pk = None):
        query_set = Clinic.objects.all ()
        clinic = get_object_or_404 (query_set , pk = pk)
        serializer = ClinicSerializer (clinic)
        return Response (serializer.data)
    
    def create (self , request):
        serializer = ClinicSerializer (data = request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self , request , pk = None):
        try :
            clinic = Clinic.objects.get (pk = pk)
        except :
            return Response (status=status.HTTP_404_NOT_FOUND)
        clinic.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT)
        
    
from django.shortcuts import render
from rest_framework import generics
from .models import Alert , Previous_Test , Provinces , Submitted_Results , Device_Results , Blog
from .serializers import Submitted_ResultsSerializer , Device_ResultsSerializer , BlogSerializer, ProvincesSerializer , Previous_TestSerializer , AlertSerializer
# Create your views here.

# LISTING
#----------

class Submitted_ResultsList(generics.ListAPIView):
    queryset = Submitted_Results.objects.all()
    serializer_class = Submitted_ResultsSerializer

class Device_ResultsList(generics.ListAPIView):
    queryset = Device_Results.objects.all()
    serializer_class = Device_ResultsSerializer

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ProvincesList(generics.ListAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class Previous_TestList(generics.ListAPIView):
    queryset = Previous_Test.objects.all()
    serializer_class = Previous_TestSerializer

class AlertList(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    

# CREATING 
#----------


class Submitted_ResultsListCreate(generics.ListCreateAPIView):
    queryset = Submitted_Results.objects.all()
    serializer_class = Submitted_ResultsSerializer

class Device_ResultsListCreate(generics.ListCreateAPIView):
    queryset = Device_Results.objects.all()
    serializer_class = Device_ResultsSerializer

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ProvincesListCreate(generics.ListCreateAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class Previous_TestListCreate(generics.ListCreateAPIView):
    queryset = Previous_Test.objects.all()
    serializer_class = Previous_TestSerializer

class AlertListCreate(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


# UPDATING OR DELETING 
#----------

class Submitted_ResultsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submitted_Results.objects.all()
    serializer_class = Submitted_ResultsSerializer
    lookup_field = "pk"

class Device_ResultsUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device_Results.objects.all()
    serializer_class = Device_ResultsSerializer
    lookup_field = "pk"

class BlogUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class ProvincesUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer
    lookup_field = "pk"

class Previous_TestUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Previous_Test.objects.all()
    serializer_class = Previous_TestSerializer
    lookup_field = "pk"

class AlertUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = "pk"
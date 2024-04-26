from rest_framework import serializers
from .models import Alert , Previous_Test , Provinces , Submitted_Results , Device_Results , Blog

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["id", "location", "details" , "date"]

class Previous_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previous_Test
        fields = ["id", "submitted", "device_test" , "user"]

class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = ["id", "province", "positive_cases" , "deaths", "cures"]

class Submitted_ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submitted_Results
        fields = ["id", "result", "location" , "image", "date", "user"]

class Device_ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device_Results
        fields = ["id", "result", "location" , "image", "date", "user"]

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "image", "title" , "details", "authors", "sources", "date"]


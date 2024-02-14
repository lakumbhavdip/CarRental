from rest_framework import serializers
from .models import Car

   
# list label language serializer
class car_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = '__all__'    
    
    
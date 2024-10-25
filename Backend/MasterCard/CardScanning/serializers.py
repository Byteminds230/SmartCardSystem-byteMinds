from rest_framework import serializers
from .models import *

class CardSerializer(serializers.ModelSerializer):
                  class Meta:
                          model = Card
                          fields = '__all__'

class ScanDeviceserializer(serializers.ModelSerializer):
        class Meta:
                model = ScanDevice
                fields = '__all__'

class CardScanserializer(serializers.ModelSerializer):
        class meta:
                model = CardScan
                fields = '__all__' 
from rest_framework import serializers
from .models import *

class customUserSerializer(serializers.ModelSerializer):
                  class Meta:
                          model = CustomUser
                          fields = ['name' , 'username', 'email' , 'password','Class','profile','role' ]

class ClassSerializer(serializers.ModelSerializer):
        class Meta:
                model = Class
                fields = '__all__'
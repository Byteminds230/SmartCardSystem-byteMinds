from rest_framework import viewsets
from .serializers import *

class UserView(viewsets.ModelViewSet):
                  queryset = CustomUser.objects.all()
                  serializer_class = customUserSerializer

class ClassView(viewsets.ModelViewSet):
        queryset = Class.objects.all()
        serializer_class = ClassSerializer
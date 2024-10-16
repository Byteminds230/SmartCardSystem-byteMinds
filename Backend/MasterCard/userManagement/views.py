from rest_framework import viewsets
from .serializers import *

class UserView(viewsets.ModelViewSet):
                  queryset = CustomUser.objects.all()
                  serializer_class = customUserSerializer
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import *
user = DefaultRouter()
user.register('',UserView , basename='users' )

Class = DefaultRouter()
Class.register('' , ClassView , basename='classes')

urlpatterns = [
    path('users/', include(user.urls)),
    path('class/', include(Class.urls)), 

]

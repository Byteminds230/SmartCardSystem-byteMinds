from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import UserView
user = DefaultRouter()
user.register('',UserView , basename='users' )

urlpatterns = [
    path('users/', include(user.urls))
]

from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serilizers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Index (viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= Studentserilizer
    authentication_classes= [JWTAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]


from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Latvanyossag, Telepules
from .serializers import LatvanyossagSerializer, TelepulesSerializer

import random
# Create your views here.
@api_view(["GET", "POST"])
def latvanyossagData(request):
    if(request.method == "GET"):
        allLatvanyossag = Latvanyossag.objects.all().order_by("Nev")
        serialized = LatvanyossagSerializer(allLatvanyossag, many= True)
        return Response(serialized.data)
    if(request.method == "POST"):
         serialized = LatvanyossagSerializer(data=request.data)
         if serialized.is_valid():
             serialized.save()
             return Response(serialized.data,status.HTTP_201_CREATED)
         return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def telepulesData(request):
    if request.method == "GET":
        allTelepules = Telepules.objects.all().order_by("Nev")
        serialized = TelepulesSerializer(allTelepules, many= True)
        return Response(serialized.data)

@api_view(["DELETE"])
def deleteLatvanyossag(request,LatId):
    if request.method == "DELETE":
        searchedLatvanyossag = Latvanyossag.objects.get(pk=LatId)
        searchedLatvanyossag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

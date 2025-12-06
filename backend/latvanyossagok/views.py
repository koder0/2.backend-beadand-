from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Latvanyossag, Telepules, Orszag
from .serializers import LatvanyossagSerializer, TelepulesSerializer, LatvanyossagSerializerPOST, TelepulesSerializerPOST, OrszagSerializer, OrszagSerializerPOST

import random
# Create your views here.
@api_view(["GET", "POST"])
def latvanyossagData(request):
    if(request.method == "GET"):
        allLatvanyossag = Latvanyossag.objects.all().order_by("Nev")
        serialized = LatvanyossagSerializer(allLatvanyossag, many= True)
        return Response(serialized.data)
    if(request.method == "POST"):
         serialized = LatvanyossagSerializerPOST(data=request.data)
         if serialized.is_valid():
             serialized.save()
             return Response(serialized.data,status.HTTP_201_CREATED)
         return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def telepulesData(request):
    if request.method == "GET":
        allTelepules = Telepules.objects.all().order_by("Nev")
        serialized = TelepulesSerializer(allTelepules, many= True)
        return Response(serialized.data)
    if(request.method == "POST"):
         serialized = TelepulesSerializerPOST(data=request.data)
         if serialized.is_valid():
             serialized.save()
             return Response(serialized.data,status.HTTP_201_CREATED)
         return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def orszagData(request):
    if request.method == "GET":
        allOrszag = Orszag.objects.all().order_by("Nev")
        serialized = OrszagSerializer(allOrszag, many= True)
        return Response(serialized.data)
    if(request.method == "POST"):
         serialized = OrszagSerializerPOST(data=request.data)
         if serialized.is_valid():
             serialized.save()
             return Response(serialized.data,status.HTTP_201_CREATED)
         return Response(serialized.errors,status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def deleteLatvanyossag(request,LatId):
    if request.method == "DELETE":
        searchedLatvanyossag = Latvanyossag.objects.get(pk=LatId)
        searchedLatvanyossag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def deleteOrszag(request,OrId):
    if request.method == "DELETE":
        searchedOrszag = Orszag.objects.get(pk=OrId)
        searchedOrszag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def deleteTelepules(request,TelepId):
    if request.method == "DELETE":
        searchedTelepules = Telepules.objects.get(pk=TelepId)
        searchedTelepules.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

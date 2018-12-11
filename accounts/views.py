from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer

class SignupView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": True,
                "message": "Successfuly Created",
                "user": serializer.data
            }
            return JsonResponse(respose_data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def get(self, request,format=None):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse({'users': serializer.data})
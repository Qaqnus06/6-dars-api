from django.shortcuts import render
from django.contrib.auth import views
from rest_framework .views  import  APIView
from .serializers import LoginSerializer, RegistrationSerializer, CodeVerificationSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import EmailVerification




class CodeVerificationApiView(APIView):
    def post(self, request):
        serializer = CodeVerificationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']

            if not EmailVerification.objects.filter(email=email, code=code).exists():
                return Response({"message": "Noto'g'ri kod kiritdingiz."}, status=400)
            
            
            return Response({"message": "kiritgan ko'dingiz mos keldi."})
        
        return Response(serializer.errors, status=400)



class LoginApiView(APIView):
    def post(self,request):
        data=request.data
        serializer=LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user=authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user in None:
            data={
                "status":False,
                "message":"used not found"
            }

            return Response(data)
        refresh = RefreshToken.for_user(user)

        data={
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response (data)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            if User.objects.filter(username=username).exists():
                return Response({"message": "allaqachon bor "})
            
            user = User.objects.create_user(username=username, email=email, password=password)
             
            return Response({"message": "yasaldi"})
        return Response(user)   


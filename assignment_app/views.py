from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .task import send_welcome_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public endpoint"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello, {request.user.username}"})

@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

    user = User.objects.create_user(username=username, password=password, email=email)

    send_welcome_email.delay(email)

    return Response({'message': 'User registered and email will be sent.'})

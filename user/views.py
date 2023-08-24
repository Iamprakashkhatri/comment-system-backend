from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, viewsets


from .serializers import *


class ObtainAuthTokenView(ObtainAuthToken):
    serializer_class = UserAuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        return Response(
            {
                "message": "Success",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user_serializer.data,
            },
            status.HTTP_200_OK,
        )

class RegisterUserAPIView(CreateAPIView):
    """
    API View for registration.
    """

    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data,context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop('confirm_password')
        user = User.objects.create(**serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        
        return Response(
                {   
                    "success": "true",
                    "message": "Great! You have signed up successfully",
                    "refresh_token": str(refresh),
                    "access_token": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                },
                status.HTTP_200_OK,
            )
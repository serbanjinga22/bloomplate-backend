from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from knox.models import AuthToken
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from .models import User

class RegisterAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })
    
class LoginAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            print(serializer.validated_data)
            if user:
                _, token = AuthToken.objects.create(user)
                return Response({
                    'token': token,
                    'user': UserSerializer(user).data
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CurrentUserAPI(generics.RetrieveUpdateAPIView):
    """ 
    API view class for getting the current user.
    
    Attributes:
        permission_classes (list): A list of permission classes that the view requires.
        serializer_class (Serializer): The serializer class used by the view, which is the UserSerializer.
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    # Overrides the get_object method to always return the currently authenticated user.
    def get_object(self):
        return self.request.user

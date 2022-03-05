from authen.serializers import (
    RegisterSerializer, 
    LoginSerializer,
    AccountAddressSerializer,
)
from rest_framework.viewsets import ModelViewSet
from authen.models import Account, AccountAddress
from rest_framework import generics, response, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class RegsiterAPI(generics.CreateAPIView):
    """Regsiter User i.e., Signup"""
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    """Login User"""
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({"message":"Invalid credentials. Try again."}, status=status.HTTP_401_UNAUTHORIZED)


class AccounstAddressViewset(ModelViewSet):
    """Viewset for create, list, retrieve, update and destroy"""
    serializer_class = AccountAddressSerializer
    queryset = AccountAddress.objects.all()

    # def get_queryset(self):
    #     account = Account.objects.get(user=user)
    #     return AccountAddress.objects.filter(account)

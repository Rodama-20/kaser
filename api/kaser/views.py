from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from oauth2_provider.models import AccessToken

from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["post"],
        url_path="register",
        serializer_class=None,
        permission_classes=[permissions.AllowAny],
    )
    def register(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        check_password = request.data.get("check_password")

        if not username or not password or not check_password:
            return Response(
                {"error": "Username and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if password != check_password:
            return Response(
                {"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST
            )
            
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        user = User.objects.create_user(username=username, password=password)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
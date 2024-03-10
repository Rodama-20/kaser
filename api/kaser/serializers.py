from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Photo, Album 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "url",
            "username",
            "email",
            "first_name",
            "last_name",            
        ]

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "url",
            "album",
            "title",
            "description",
            "file",
            "date_uploaded",
        ]

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = [
            "id",
            "url",
            "title",
            "description",
            "date_created",
        ]

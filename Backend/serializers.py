from rest_framework import serializers
from django.contrib.auth.models import User
from .models import File, Comments
from rest_framework.authtoken.views import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password'
        )

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class FileSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    fileType = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    rating = serializers.StringRelatedField()
    cast = serializers.StringRelatedField()
    prefix = serializers.StringRelatedField()

    class Meta:
        model = File
        fields = (
            'id', 'title', 'genre', 'imageArt', 'prefix', 'onDisplay', 'description', 'releaseDate', 'downloadable', 'fileType', 'author', 'artiste', 'rating', 'cast', 'date_uploaded'
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            'id', 'name', 'comment', 'email', 'comment_file'
        )
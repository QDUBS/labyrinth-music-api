from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, FileSerializer, CommentSerializer
from .models import File, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


class File(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class Comment(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            comment = serializer.data.get('comment')
            email = serializer.data.get('email')
            comment_file = serializer.data.get('comment_file')

            comments = Comments(name=name, comment=comment, email=email, comment_file=comment_file)
            comments.save()

        return Response(CommentSerializer(comments).data, status=status.HTTP_201_CREATED)

class User(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
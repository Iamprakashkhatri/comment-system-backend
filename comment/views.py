from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *

class CommentViewset(viewsets.ModelViewSet):
    
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    http_method_names = [
    	"get",
        "post",
    ]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(
            {"message": "Successfully Retrieved Comment", "data": CommentSerializer(obj).data}, status.HTTP_201_CREATED
        )

class ReplyViewset(viewsets.ModelViewSet):
    
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    http_method_names = [
    	"get",
        "post",
    ]

    def create(self, request):
        print('teset------')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(
            {"message": "Successfully Retrieved Reply", "data": ReplySerializer(obj).data}, status.HTTP_201_CREATED
        )
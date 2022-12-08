from rest_framework import serializers

from .models import (
    Comment,
    Reply
)

class ReplySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Reply
        fields = ("id","user","comment","description","username","created_at")
        read_only_fields = ("id",)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    replies = ReplySerializer(source="comment_reply", many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ("id","user","description","replies","username","created_at")
        read_only_fields = ("id",)


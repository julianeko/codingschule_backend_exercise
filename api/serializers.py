from .models import Like, Post
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields =["post"]

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    likes = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        # fields="__all__"
        exclude = ["author"]

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = "__all__"
       

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["text"]



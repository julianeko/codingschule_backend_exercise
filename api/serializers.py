from .models import Post
from .models import User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
       

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "text"]

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User

    

# class PostSerializer(serializers.ModelSerializer):
#         user = UserSerializer()
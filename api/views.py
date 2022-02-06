from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Like
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, NewPostSerializer, LikeSerializer
from django.shortcuts import redirect
from django.core import serializers
# from api import serializers
from rest_framework import status
from rest_framework.views import APIView




def index(request):

    post = Post.objects.all()

    context = {
    "post" : post
    }
   # return HttpResponse("Hello World")
    return render(request, "api/index.html", context)
    

def api_get(request):
    posts = Post.objects.all()
    data = serializers.serialize("json", posts)
    return HttpResponse(data)

def api_new(request, author):
    newtext = request.GET["text"]
    new_post = Post(author=author, text=newtext)
    new_post.save()
    
    return redirect("/")




@api_view(["POST", "GET"])
# @permission_classes([IsAuthenticated])
def api(request):
    if request.method == 'POST':
        # Nuer Post
        # request.data
        # new_post = Post()
        # new_post.save()
        # alle Post
        print("Hallo alt")
        
       
        new_Post = NewPostSerializer(data=request.data)
        # new_Post.user = request.user
        if new_Post.is_valid(raise_exception=True):
            # text=new_Post.data.get("text")
            print(request.data)
            # user=request.user
            # new_Post = Post(user=request.user, text=request.text)
            new_Post.save(user=request.user)

    post = Post.objects.all()
    post = post.order_by("-created_at")
    serializer= PostSerializer(post, many=TRUE)

       
    return Response(serializer.data)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def likes(request):
    userID = request.user
    postID = request.data["post"]
    data = Like.objects.filter(post=postID,user=userID)
    if data.exists():
        data.delete()
        print("dislike")
    else: 
        post = Post.objects.get(id=postID)
        new_Like = Like(post=post,user=userID)
        new_Like.save()
        print("like")
      
 
  
    return Response()



# def example_view(request, format =None): 
#     content = {"status": "request was permitted"}
#     return Response(content)
        

# class CreatePostView(APIView):
#     serializer_class = NewPostSerializer
#     def post(self, request, format=None):
#         print("Hallo neu")
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#                     text=serializer.data.get("text")
#                     user=request.user
#                     post = Post(user=user, text=text)
#                     post.save()
                    
#                     return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
#         return Response ({"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST)
   







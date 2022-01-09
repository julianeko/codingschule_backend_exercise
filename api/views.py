from django.shortcuts import render

from django.http import HttpResponse

from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.shortcuts import redirect
from django.core import serializers
from api import serializers

# from django.http import HttpResponse
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# Create your views here.

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


@api_view()
def api(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)




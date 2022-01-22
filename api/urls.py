from django.urls import path
from api import views




urlpatterns = [
    path("", views.index, name="index"),
    path("api/posts", views.api_get),
    path("api", views.api, name="api"),
    path("new", views.api_new, name="api_new")
      ]



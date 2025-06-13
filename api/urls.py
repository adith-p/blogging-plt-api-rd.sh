from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:pk>", views.PostView.as_view(), name="posts"),
    path("posts/", views.PostsView.as_view(), name="posts"),
]

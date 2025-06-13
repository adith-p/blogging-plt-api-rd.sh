from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from . import models
from .serializers import PostSerializer

# Create your views here.


class PostsView(APIView):

    def get(self, request):
        term = request.query_params.get("term", None)
        if term:
            post = models.Post.objects.filter(
                Q(title__contains=term)
                or Q(content__contains=term)
                or Q(category__contains=term)
                or Q(tags__name__contains=term)
            )
            if post.exists():
                serializer = PostSerializer(post, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        posts = models.Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):

    def get(self, request, pk):
        try:
            post = models.Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.Post.DoesNotExist:
            return Response(
                {"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk):
        try:
            post = models.Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Post.DoesNotExist:
            return Response(
                {"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        try:
            post = models.Post.objects.get(pk=pk)

        except models.Post.DoesNotExist:
            return Response(
                {"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND
            )
        post.delete()
        return Response(
            {"detail": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

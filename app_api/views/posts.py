"""View module for handling requests about zas_users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from app_api.models.zas_user import ZASUser
from app_api.models.post import Post


class PostView(ViewSet):
    """View for handling Post requests"""

    def retrieve(self, request, pk):
        """GET method handler for single object"""
        try:
            post = Post.objects.get(pk=pk)
            serializer = RepliesByPostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET list of all posts"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST Post handler"""
        author = ZASUser.objects.get(user=request.auth.user)
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author)
        post = Post.objects.get(pk=serializer.data['id'])
        post.tags.add(*request.data['tags'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """DELETE request handler for Post"""
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for Posts
    The serializer class determines how the Python data should
    be serialized to be sent back to the client.
    """
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'created_on',
            'body',
            'tags'
        )


class RepliesByPostSerializer(serializers.ModelSerializer):
    """JSON serializer to get a single Post with all Replies that share a fk"""
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'created_on',
            'body',
            'tags',
            'replies'
        )
        depth = 1


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'created_on',
            'body',
            'tags',
            'tagged')

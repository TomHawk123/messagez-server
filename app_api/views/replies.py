"""View module for handling requests about zas_users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
# from rest_framework.decorators import action
from app_api.models.zas_user import ZASUser
from app_api.models.reply import Reply
from app_api.models.post import Post


class ReplyView(ViewSet):
    """View for handling Reply Requests"""

    def retrieve(self, request, pk):
        """GET method handler to receive single object"""
        try:
            reply = Reply.objects.get(pk=pk)
            serializer = ReplySerializer(reply)
            return Response(serializer.data)
        except Reply.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET method handler to list all objects"""
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request handler"""
        # data is a dict, must us bracket notation.
        # to filter the user object, use dunder in syntax below.
        # WHERE username=username in data dict ("filter")
        respondent = ZASUser.objects.get(user=request.auth.user)
        serializer = CreateReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(respondent=respondent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """DELETE request handler"""
        reply = Reply.objects.get(pk=pk)
        reply.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

    # @action(methods=['get'], detail=True, url_path="/posts/{id}")
    # def post_replies(self, request):
    #     """GET replies for a given Post
    #     Args:
    #         request (_type_): _description_
    #     """
    #     replies = Reply.objects.filter(post_id=request.data)
    #     serializer = ReplySerializer(replies, many=True)
    #     return Response(serializer.data)


class ReplySerializer(serializers.ModelSerializer):
    """JSON serializer for GET replies"""
    class Meta:
        model = Reply
        fields = (
            'id',
            'post',
            'respondent',
            'content',
            'created_on'
        )


class CreateReplySerializer(serializers.ModelSerializer):
    """JSON Serializer for POST and PUT replies"""
    class Meta:
        model = Reply
        fields = (
            'post',
            'content',
            'created_on'
        )

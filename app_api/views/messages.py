"""View module for handling requests about zas_users"""
from django.http import HttpResponseServerError
from django.db.models import Q
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from app_api.models.message import Message
from app_api.models.zas_user import ZASUser



class MessageView(ViewSet):
    """View for handling Message requests"""

    def retrieve(self, request, pk):
        """GET method handler to receive single object"""
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET method handler to receive all objects"""
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request handler"""
        sender = ZASUser.objects.get(user=request.auth.user)
        # data is a dict, must us bracket notation.
        # to filter the user object, use dunder in syntax below.
        # WHERE username=username in data dict ("filter")
        recipient = ZASUser.objects.get(
            user__username=request.data['username'])
        serializer = CreateMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sender=sender, recipient=recipient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """DELETE request handler"""
        message = Message.objects.get(pk=pk)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def inbox(self, request):
        """GET messages for a signed in user"""
        messages = Message.objects.filter(Q(sender=request.auth.user.id) | Q(recipient=request.auth.user.id))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for Messages"""
    class Meta:
        model = Message
        fields = (
            'id',
            'sender',
            'content',
            'recipient',
            'created_on'
        )


class CreateMessageSerializer(serializers.ModelSerializer):
    """JSON serializer for Messages"""
    class Meta:
        model = Message
        fields = (
            'content',
            'created_on'
        )

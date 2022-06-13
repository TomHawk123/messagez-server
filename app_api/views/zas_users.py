"""View module for handling requests about zas_users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import ZASUser


class ZASUserView(ViewSet):
    """ZasUser view"""

    def retrieve(self, request, pk):
        """retrieve single ZASUser object"""
        try:
            zas_user = ZASUser.objects.get(pk=pk)
            serializer = ZASUserSerializer(zas_user)
            return Response(serializer.data)
        except ZASUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """list all ZASUser objects"""
        zas_user = ZASUser.objects.all()
        serializer = ZASUserSerializer(zas_user, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Update a single zas_user object with PUT"""
        zas_user = ZASUser.objects.get(pk=pk)
        serializer = CreateZASUserSerializer(zas_user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE method for a zas_user"""
        zas_user = ZASUser.objects.get(pk=pk)
        zas_user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ZASUserSerializer(serializers.ModelSerializer):
    """JSON serializer for listing, retrieving, and deleting ZASUser"""
    class Meta:
        model = ZASUser
        fields = (
            'id',
            'name',
            'title',
            'bio',
            'user',
            'created_on'
        )


class CreateZASUserSerializer(serializers.ModelSerializer):
    """ JSON serializer for updating and creating ZASUsers"""
    class Meta:
        model = ZASUser
        fields = (
            'name',
            'title',
            'bio',
            'created_on'
        )

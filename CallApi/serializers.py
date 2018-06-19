from django.db import models
# from django import forms
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Call, Album


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class CallSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = models
#         fields = ('record_type', 'record_timestamp', 'call_identifier', 'origin_phone_number', 'destination_phone_number')

# https://www.youtube.com/watch?v=r9kT-jm136Q To watch later

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
        # fields = ('url', 'username')

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('url', 'record_type', 'call_identifier', 'origin_phone_number', 
        			'destination_phone_number', 'record_timestamp', 'duration')
from re import S
from rest_framework import serializers


class DummyResponseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    surname = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

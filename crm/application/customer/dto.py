from rest_framework import serializers


class CustomerResponseDto(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=100)


class CustomerCreateRequestDto(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=100)


class CustomerUpdateRequestDto(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=100)

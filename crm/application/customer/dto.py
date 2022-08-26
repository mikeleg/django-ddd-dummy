from rest_framework import serializers

class CustomerResponseDto(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    surname = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=40)
    email = serializers.EmailField(max_length=100)
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
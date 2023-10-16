from rest_framework import serializers

class Bookserializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    edition = serializers.IntegerField()
    publisher = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)


from rest_framework import serializers

from .models import User, Dog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Dog
        # fields = ('name')
        fields = '__all__'

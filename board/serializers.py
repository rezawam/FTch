from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostForm
        fields = ['text']
        
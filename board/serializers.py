from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'text',
            'parent',
            'pub_date',
            'board',
            'reply_to'
        )

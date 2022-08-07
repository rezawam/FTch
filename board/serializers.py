from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post_text',
            'parent_post_id',
            'pub_date',
            'board',
        )

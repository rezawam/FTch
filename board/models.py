from django.db import models
from django.forms import ModelForm


class Post(models.Model):
    post_text = models.TextField()
    pub_date = models.DateTimeField()
    board = models.CharField(max_length=5)
    parent_post_id = models.IntegerField(default=0)

    def __str__(self):
        return self.post_text

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_text']

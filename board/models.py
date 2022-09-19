from django.db import models
from django.forms import ModelForm
from django.utils import timezone


BOARDS = {'b': 'Бред', 'soc': 'Общение', 'un': 'Образование'}
now = timezone.localtime(timezone.now())


class Post(models.Model):
    text = models.TextField(max_length=15000)
    title = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(auto_now_add=now)
    board = models.CharField(max_length=5)
    # img = models.ImageField(upload_to='post', null=True, blank=True)
    parent = models.ForeignKey("self",
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               )  # Able to assign only while creating
    reply_to = models.ForeignKey("self",
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='replies',
                                 )  # Able to assign only while creating

    def __str__(self):
        return self.text


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        # fields = ['text', 'title']

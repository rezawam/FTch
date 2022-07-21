from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic

from .models import PostForm, Post

class PostView(generic.DetailView):
    model = Post
    template_name = 'board/post.html'


def get_post(request):  # refactor to CBV
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.pub_date = timezone.now()
            new_post.board = 'b'
            new_post.save()
            return HttpResponseRedirect('/b/')
    else:
        form = PostForm()
    return render(request, 'board/index.html', {
        'form': form,
        'posts': posts,
})



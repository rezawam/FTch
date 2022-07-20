from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import PostForm

def get_post(request):
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
    return render(request, 'board/index.html', {'form': form})


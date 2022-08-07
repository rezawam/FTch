from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils import timezone
from django.views import generic
from datetime import timedelta

from rest_framework import generics

from .models import *
from .serializers import PostSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def get_board_view(request, brd):
    if brd not in BOARDS.keys():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    posts = reversed(Post.objects.filter(parent_post_id=0, board=brd))
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.board = brd
            new_post.save()
            return HttpResponseRedirect(f'/{brd}/')
    else:
        form = PostForm()
    return render(request, 'board/index.html', {
        'form': form,
        'posts': posts,
        'brd': brd,
        'board_name': BOARDS[brd],
        'title': f'/{brd}/ – {BOARDS[brd]}'
})

def get_post_view(request, pk, brd):  # refactor to CBV
    if brd not in BOARDS:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if Post.objects.filter(pk=pk, board=brd).exists():
        post = Post.objects.get(pk=pk, board=brd)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if post.parent_post_id != 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    comments = Post.objects.filter(parent_post_id=pk, board=brd)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.pub_date = timezone.now() + timedelta(hours=3)
            new_post.parent_post_id = pk
            new_post.board = brd
            new_post.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, 'board/post.html', {
        'comments': comments,
        'p': post,
        'title': f'/{brd}/ – Тред',
        'board_name': BOARDS[brd],
    })



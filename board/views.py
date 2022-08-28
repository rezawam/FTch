from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class PostAPIView(APIView):

    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']

    def get(self, request):
        posts = Post.objects.all()
        serializer_for_queryset = PostSerializer(
            instance=posts,
            many=True,
        )
        return Response(serializer_for_queryset.data)

    # def post(self, request):


def get_board_view(request, brd):
    if brd not in BOARDS.keys():
        return HttpResponseNotFound('<h1>Page not found</h1>')
    posts = reversed(Post.objects.filter(board=brd, parent=None))
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
        'title': f'/{brd}/ – {BOARDS[brd]}',

})

def get_post_view(request, pk, brd):
    if brd not in BOARDS:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if Post.objects.filter(pk=pk, board=brd).exists():
        post = Post.objects.get(pk=pk, board=brd)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if post.parent is not None:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    comments = post.comments.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.parent = post
            new_post.board = brd
            new_post.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, 'board/post.html', {
        'comments': comments,
        'p': post,
        'title': f'/{brd}/ – Тред',
        'board_name': BOARDS[brd],
    })



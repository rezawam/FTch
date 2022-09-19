from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

def get_board_view(request, brd):
    posts = Post.objects.filter(board=brd)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


def get_post(request, pk):
    posts = Post.objects.get(pk=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)


def create_post(request):
    data = request.data
    post = Post.objects.create(
        text=data['text'],
        board=data['board'],
        parent=data['parent'],
        reply_to=data['reply_to']
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)




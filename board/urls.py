from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.get_board_view, name='index'),
    path('thread/<int:pk>', views.get_post_view, name='post'),
]

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'board'

urlpatterns = [
    path('', views.get_board_view, name='index'),
    path('thread/<int:pk>', views.get_post_view, name='post'),
]

urlpatterns += staticfiles_urlpatterns()

from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.get_post, name='index'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
]

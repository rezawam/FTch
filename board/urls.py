from django.urls import path
from board import views

urlpatterns = [
    path('', views.get_post),
    path('res/', )
    # path("hello/<name>", views.hello_there, name="hello_there"),
]

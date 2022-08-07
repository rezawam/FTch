from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'board/home.html', {
        'title': 'MIPTchan',
    })
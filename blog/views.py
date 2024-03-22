from django.shortcuts import render
from datetime import datetime
posts = [
  {'author': 'amine',
  'title': "first post's title",
  'content': "first post's content",
  'date': datetime.now()},
  {'author': 'james',
  'title': "second post's title",
  'content': "second post's content",
  'date': datetime.now()}
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
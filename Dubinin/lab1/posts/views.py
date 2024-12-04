from django.shortcuts import render
from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.get(slug=slug)
    return render(request, 'posts/posts_list.html', {'posts': posts})
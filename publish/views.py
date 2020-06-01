from django.shortcuts import render
from django.http import Http404
from .models import Post
# Create your views here.

def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'post.html', {'post': post})

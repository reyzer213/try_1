from django.shortcuts import render, get_object_or_404
from .models import Post, Author


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    try:
        author = get_object_or_404(Author, pk=author_id)
        posts = Post.objects.filter(author=author)
        return render(request, 'posts_by_author.html', {'author': author, 'posts': posts})
    except Author.DoesNotExist:
        return render(request, 'author_not_found.html', {'author_id': author_id})
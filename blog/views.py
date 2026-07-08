from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from .models import Post

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No post found.")
    return render(request, 'blog/post/detail.html', {'post': post})

def post_list(request):
 
    posts_list = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-id')
    

    paginator = Paginator(posts_list, 3)
    

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
 
    return render(request, 'web/blog.html', {'posts': posts})
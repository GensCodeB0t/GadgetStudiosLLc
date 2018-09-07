from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_home.html', {'blogs':blogs})

def detail(request, blog_id):
    blogDetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blogDetail})

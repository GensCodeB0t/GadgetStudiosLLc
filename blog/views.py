from django.shortcuts import render, get_object_or_404
from social_networks.models import Social_Network
from frontpage.models import Front_Page
from .models import Blog

def blog_home(request):
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    blogs = Blog.objects.all()

    blogs = list(blogs)

    number_of_blogs = len(blogs)
    if number_of_blogs < 6:
        for i in range(number_of_blogs, 6):
            blogs.append(Blog(title='Coming Soon...', image_thumbnail='projects/ComingSoon.png', \
            body='Coming Soon...', author='', pub_date='coming soon...' ))

    return render(request, 'blog/blog_home.html', { 'blogs':blogs, 'front_page':front_page, 'social_networks':social_networks })

def blog_detail(request, blog_id):
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    blogDetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', { 'blog':blogDetail, 'front_page':front_page, 'social_networks':social_networks })

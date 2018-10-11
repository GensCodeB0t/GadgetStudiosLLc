from django.shortcuts import render
from prg_languages.models import Prg_Language
from services_provided.models import Service_Provided
from social_networks.models import Social_Network
from frontpage.models import Front_Page
from projects.models import Project
from blog.models import Blog
from datetime import datetime
from .models import Job


def home(request):
    prg_languages = Prg_Language.objects.all()
    jobs = Job.objects.all()
    services_provided = Service_Provided.objects.all()
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    services = services_provided

    blogs = sorted(Blog.objects.all(), key=lambda x: x.pub_date)[:3]
    number_of_blogs = len(blogs)
    if number_of_blogs < 3:
        for i in range(number_of_blogs, 3):
            blogs.append(Blog(title='Coming Soon..', pub_date=datetime.today(), \
            body='Coming Soon', author='Gadget', image='blogimages/ComingSoon.png'))


    categories = []
    for project in(project for project in Project.objects.all() if project.category not in categories):
        categories.append(project.category)

    projects= []
    category_count = 0
    for category in categories:
        category_count = 0
        for project in(project for project in sorted(Project.objects.all(), key=lambda x: x.pub_date) if project.category in category):
            if category_count < 2:
                projects.append(project)
                category_count += 1
            else:
                break

    number_of_projects = len(projects)
    if number_of_projects < 6:
        for i in range(number_of_projects, 6):
            projects.append(Project(title='Coming Soon...', image_thumbnail='projects/ComingSoon.png', \
            description='Coming Soon...', link='', category='coming soon...' ))


    return render(request, 'jobs/home.html', { 'languages': prg_languages, 'jobs': jobs, \
    'services_provided':services_provided, 'social_networks':social_networks, 'front_page':front_page, \
    'projects':projects, 'blogs':blogs } )

from django.shortcuts import render, get_object_or_404
from frontpage.models import Front_Page
from social_networks.models import Social_Network
from .models import Project

def project_home(request):
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    projects = Project.objects.all()

    projects = list(projects)

    number_of_projects = len(projects)
    if number_of_projects < 6:
        for i in range(number_of_projects, 6):
            projects.append(Project(title='Coming Soon...', image_thumbnail='projects/ComingSoon.png', \
            description='Coming Soon...', link='', category='coming soon...' ))

    return render(request, 'project/project_home.html', { 'projects':projects, 'front_page':front_page, 'social_networks':social_networks })

def project_detail(request, project_id):
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    projectDetail = get_object_or_404(Project, pk=project_id)
    return render(request, 'project/project_detail.html', { 'project':projectDetail, 'front_page':front_page, 'social_networks':social_networks })

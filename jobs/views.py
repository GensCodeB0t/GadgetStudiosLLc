from django.shortcuts import render
from prg_languages.models import Prg_Language
from services_provided.models import Service_Provided
from social_networks.models import Social_Network
from frontpage.models import Front_Page
from .models import Job

def home(request):
    prg_languages = Prg_Language.objects.all()
    jobs = Job.objects.all()
    services_provided = Service_Provided.objects.all()
    social_networks = Social_Network.objects.all()
    front_page = Front_Page.objects.first()
    services = services_provided
    return render(request, 'jobs/home.html', { 'languages': prg_languages, 'jobs': jobs, \
    'services_provided':services_provided, 'social_networks':social_networks, 'front_page':front_page } )

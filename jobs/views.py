from django.shortcuts import render
from prg_languages.models import Prg_Language
from .models import Job

def home(request):
    prg_languages = Prg_Language.objects.all()
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'languages': prg_languages, 'jobs': jobs} )

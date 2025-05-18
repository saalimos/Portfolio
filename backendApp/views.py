from django.shortcuts import render
from backendApp.models import ProfileDB, TechStackDB, ProjectDB, QualificationDB,ExperienceDB

# Create your views here.
def indexpage(request):
    profile = ProfileDB.objects.all().first()  # Assuming only one profile
    tech = TechStackDB.objects.all()
    projects = ProjectDB.objects.all()
    qualification = QualificationDB.objects.all()
    experience = ExperienceDB.objects.all()

    
    # Add description list to each experience
    experience_list = []
    for exp in experience:
        exp.description_lines = exp.desc.strip().splitlines()
        experience_list.append(exp)

    context = {
        'profile': profile,
        'tech': tech,
        'projects': projects,
        'qualification': qualification,
        'experience' : experience_list,
        'spans': range(200)
    }

    return render(request, 'index.html', context)
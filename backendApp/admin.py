from django.contrib import admin

# Register your models here.
from .models import ProfileDB, ProjectDB, QualificationDB, TechStackDB ,ExperienceDB  # import your models

admin.site.register(ProfileDB)
admin.site.register(ProjectDB)
admin.site.register(QualificationDB)
admin.site.register(TechStackDB)
admin.site.register(ExperienceDB)

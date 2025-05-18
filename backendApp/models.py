from django.db import models

class ProfileDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile/',null=True,blank=True)
    role = models.CharField(max_length=100,null=True,blank=True)
    age = models.CharField(max_length=100,null=True,blank=True)
    mobile= models.CharField(max_length=100,null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)
    main_degree= models.CharField(max_length=100,null=True,blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    summary = models.TextField(null=True,blank=True)

    
    def __str__(self):
        return self.name

class ProjectDB(models.Model):
    profile = models.ForeignKey(ProfileDB, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    icon = models.FileField(upload_to='project/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

class QualificationDB(models.Model):
    profile = models.ForeignKey(ProfileDB, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100,null=True,blank=True)
    institution = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class TechStackDB(models.Model):
    profile = models.ForeignKey(ProfileDB, on_delete=models.CASCADE)
    technology = models.CharField(max_length=100)
    icon = models.FileField(upload_to='tech_icons/', null=True, blank=True)  # optional icon for each tech

    def __str__(self):
        return self.technology


class ExperienceDB(models.Model):
    profile = models.ForeignKey(ProfileDB, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100,null=True,blank=True)
    year = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
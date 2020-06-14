from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='skill_icons')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='project_pictures')
    description = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)
    team = models.CharField(max_length=200, default='')
    repository = models.CharField(max_length=200, default='')
    link = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, default='')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

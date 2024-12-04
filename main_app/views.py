from django.shortcuts import render

from django.http import HttpResponse

class Project:
    def __init__(self, name, desc, start, lang, status, link):
        self.name = name
        self.desc = desc
        self.start = start
        self.lang = lang
        self.status = status
        self.link = link


projects = [
    Project('PoetrySim', 'Simple front end JS game', '2024-09-26', 'JavaScript', 'Needs Refactoring', 'https://github.com/sara-searson/PoetrySim,'),
    Project('Ralphs Den', 'Video game collection management site', '2024-10-17', 'JavaScript', 'Needs Refactoring', 'https://github.com/sara-searson/ralphs-den'),
    Project('Sprout', 'Self improvement/Hobby finder app', '2024-11-15', 'React', 'Portfolio Ready', 'https://github.com/siseldyke/self-learner-app-front-end'),
    Project('Pulse Check', 'Project status management app', '2024-12-03', 'Django', 'In Progress', 'https://github.com/sara-searson/pulse-check-tracker'),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Engineers!</h1>')

def about(request):
    return render(request, 'about.html')

def project_index(request):
    return render(request, 'projects/index.html', {'projects': projects})
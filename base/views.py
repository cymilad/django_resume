from django.shortcuts import render
from unicodedata import category

from base.models import *


# Create your views here.
def index(request):
    socialmedias = SocailMedia.objects.first()
    hero_section = HeroSection.objects.first()
    feature = Feature.objects.all()
    aboutme = AboutMe.objects.first()
    counter = Counter.objects.all()
    skills = Skill.objects.all()
    skills_left = skills[:len(skills) // 2]
    skills_right = skills[len(skills) // 2:]
    services = Service.objects.all()
    worksexprince = WorkExpreience.objects.all()
    educations = Education.objects.all()
    items = ProtfolioItem.objects.all()
    categories = ProtfolioItem.objects.values_list('category', flat=True).distinct()

    context = {
        'hero_sction': hero_section,
        'feature': feature,
        'aboutme': aboutme,
        'counter': counter,
        'skills_left': skills_left,
        'skills_right': skills_right,
        'services': services,
        'worksexprince': worksexprince,
        'educations': educations,
        'categories': categories,
        'items': items,
        'socialmedia': socialmedias,
    }
    return render(request, 'base/home.html', context)

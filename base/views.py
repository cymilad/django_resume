from django.shortcuts import render
from base.models import *

# Create your views here.
def index(request):
    hero_section = HeroSection.objects.first()
    feature = Feature.objects.all()
    aboutme = AboutMe.objects.first()

    context = {
        'hero_sction': hero_section,
        'feature': feature,
        'aboutme': aboutme,
    }
    return render(request, 'base/home.html', context)

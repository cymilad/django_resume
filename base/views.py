from django.shortcuts import render
from base.models import *


# Create your views here.
def index(request):
    hero_section = HeroSection.objects.first()
    feature = Feature.objects.all()
    aboutme = AboutMe.objects.first()
    counter = Counter.objects.all()

    context = {
        'hero_sction': hero_section,
        'feature': feature,
        'aboutme': aboutme,
        'counter': counter,
    }
    return render(request, 'base/home.html', context)

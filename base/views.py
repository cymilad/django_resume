from django.shortcuts import render
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
    blog_posts = BlogPost.objects.all().order_by('-date')
    contact_info = ContactInfo.objects.first()
    success_message = None
    success_message_mail = None

    if request.method == "POST" and request.POST.get('subject'):

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name != "" and email != "" and phone != "" and subject != "" and message != "":
            contact_message = ContactMessage()
            contact_message.name = name
            contact_message.email = email
            contact_message.phone = phone
            contact_message.subject = subject
            contact_message.message = message
            contact_message.save()
            success_message = 'پیام شما با موفقیت ارسال شد'

    if request.method == "POST" and request.POST.get('subcriber_email'):
        print('subcriber_email')
        # subcriber mail
        subcriber_mail = request.POST.get('subcriber_email')
        subcriber = Subscribe_Email()
        subcriber.email = subcriber_mail
        subcriber.save()
        success_message_mail = 'شما با موفقیت عضو خبرنامه ایمیلی ما شدید.'



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
        'blog_posts': blog_posts,
        'contact_info': contact_info,
        'success_message': success_message,
        'success_message_mail': success_message_mail,
    }
    return render(request, 'base/home.html', context)

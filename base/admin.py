from django.contrib import admin
from base.models import *


# Register your models here.
class SocailMediaAdmin(admin.ModelAdmin):
    list_display = ['telegram', 'youtube', 'github', 'instagram']


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'exprience_years']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'address']


admin.site.register(SocailMedia, SocailMediaAdmin)
admin.site.register(HeroSection)
admin.site.register(Feature)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Counter)
admin.site.register(Skill)
admin.site.register(Service, ServiceAdmin)
admin.site.register(WorkExpreience)
admin.site.register(Education)
admin.site.register(ProtfolioItem)
admin.site.register(BlogPost)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(ContactMessage)
admin.site.register(Subscribe_Email)

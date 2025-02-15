from django.contrib import admin
from base.models import *


# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'exprience_years']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


admin.site.register(HeroSection)
admin.site.register(Feature)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Counter)
admin.site.register(Skill)
admin.site.register(Service, ServiceAdmin)
admin.site.register(WorkExpreience)
admin.site.register(Education)

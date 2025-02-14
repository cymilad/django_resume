from django.contrib import admin
from base.models import *

# Register your models here.
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'exprience_years']

admin.site.register(HeroSection)
admin.site.register(Feature)
admin.site.register(AboutMe, AboutMeAdmin)
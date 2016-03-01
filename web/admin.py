from django.contrib import admin

# Register your models here.
from web.models import Me, Social


class SocialInline(admin.TabularInline):
    model = Social
    extra = 4

class MeAdmin(admin.ModelAdmin):
    inlines = [SocialInline]

admin.site.register(Me, MeAdmin)
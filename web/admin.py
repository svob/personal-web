from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from web.models import Me, Social, BlogPost, Category, BlogTag, School, Work, Skill


class SocialInline(admin.TabularInline):
    model = Social
    extra = 0

class SchoolInline(admin.StackedInline):
    model = School
    extra = 0

class WorkInline(admin.StackedInline):
    model = Work
    extra = 0

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class MeAdmin(SingletonModelAdmin):
    inlines = [SocialInline, SkillInline, SchoolInline, WorkInline]

class BlogPostsAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags","categories")

class SchoolAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class WorkAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

class SkillAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

admin.site.register(Me, MeAdmin)
admin.site.register(BlogPost, BlogPostsAdmin)
admin.site.register(Category)
admin.site.register(Social)
admin.site.register(BlogTag)
admin.site.register(School, SchoolAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Skill, SkillAdmin)
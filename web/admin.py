from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from web.models import Me, Social, BlogPost, Category, BlogTags


class SocialInline(admin.TabularInline):
    model = Social
    extra = 4

class MeAdmin(SingletonModelAdmin):
    inlines = [SocialInline]

class BlogPostsAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags","categories")

admin.site.register(Me, MeAdmin)
admin.site.register(BlogPost, BlogPostsAdmin)
admin.site.register(Category)
admin.site.register(Social)
admin.site.register(BlogTags)
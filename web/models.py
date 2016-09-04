from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from solo.models import SingletonModel
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from hitcount.models import HitCountMixin, HitCount


# Create your models here.
class Me(SingletonModel):
    name = models.CharField(max_length=50, default='John')
    surname = models.CharField(max_length=50, default='Doe')
    photo = ImageField(upload_to='me', blank=True, null=True)
    address = models.CharField(max_length=50, default='Home Sweet Home')
    descript_short = models.CharField(max_length=200, default='hello')
    description = models.TextField(max_length=500, default='kuk')
    birth = models.DateField(default=timezone.now)
    email = models.EmailField(default='John@Doe.com')
    phone = models.CharField(max_length=20, default='777 888 999')
    skype = models.CharField(max_length=20, default='J.D.')
    languages = models.CharField(max_length=100, default='czech')
    resume = models.FileField(upload_to="me", blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Me'


class School(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    person = models.ForeignKey(Me, default=1)

    def __str__(self):
        return self.name


class Work(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    person = models.ForeignKey(Me, default=1)

    def __str__(self):
        return self.company_name

class Skill(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.IntegerField()
    icon_class = models.CharField(max_length=100)
    person = models.ForeignKey(Me, default=1)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    href = models.CharField(max_length=400)
    person = models.ForeignKey(Me, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Blog categories'


class BlogTag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'Blog tags'


class BlogPost(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    text_short = models.TextField(blank=True, null=True)
    text = RichTextUploadingField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Me, default=1)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(BlogTag)
    image = ImageField(upload_to='posts', blank=True, null=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Portfolio categories'


class PortfolioTechnologies(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    icon_image = ImageField(upload_to="portfolio/icons", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Portfolio technolgies'


class Project(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    github = models.URLField(blank=True, null=True)
    preview = models.URLField(blank=True, null=True)
    download_file = models.FileField(blank=True, null=True, upload_to="portfolio/files")
    download_url = models.URLField(blank=True, null=True)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Me, default=1)
    categories = models.ManyToManyField(PortfolioCategory)
    technologies = models.ManyToManyField(PortfolioTechnologies)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    image = ImageField(upload_to='portfolio')
    project = models.ForeignKey(Project, related_name='images')
from django.db import models
from solo.models import SingletonModel
from django.utils import timezone

# Create your models here.
class Me(SingletonModel):
    name = models.CharField(max_length=50, default='John')
    surname = models.CharField(max_length=50, default='Doe')
    photo = models.ImageField(upload_to='me', null=True)
    address = models.CharField(max_length=50, default='Home Sweet Home')
    descript_short = models.CharField(max_length=200, default='hello')
    description = models.TextField(max_length=500, default='kuk')
    birth = models.DateField(default=timezone.now)
    email = models.EmailField('John@Doe.com')
    phone = models.CharField(max_length=20, default='777 888 999')
    skype = models.CharField(max_length=20, default='J.D.')
    languages = models.CharField(max_length=100, default='czech')

    def __str__(self):
        return self.name# + self.surname

    class Meta:
        verbose_name = 'Me'

class Social(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    href = models.CharField(max_length=400)
    person = models.ForeignKey(Me, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class BlogTags(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'BlogTags'

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text_short = models.TextField(blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(Me, default=1)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(BlogTags)
    image = models.ImageField(upload_to='posts', null=True)

    def __str__(self):
        return self.title


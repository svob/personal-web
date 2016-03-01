from django.db import models

# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=20)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.name# + self.surname

    class Meta:
        verbose_name_plural = 'Me'

class Social(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    href = models.CharField(max_length=400)
    person = models.ForeignKey(Me, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
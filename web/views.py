from django.shortcuts import render
from django.views import generic

# Create your views here.
from web.models import Me


def index(request):
    me = Me.objects.all()[0]
    return render(request, 'web/index.html', { 'me':me })

def blog(request):
    return render(request, 'web/blog.html')

def portfolio(request):
    return render(request, 'web/portfolio.html')

def contact(request):
    return render(request, 'web/contact.html')

def blog_single(request, pk):
    return render(request, 'web/blog-single.html')
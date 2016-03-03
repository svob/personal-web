from django.shortcuts import render
from django.utils import timezone
from django.views import generic

# Create your views here.
from web.models import Me, BlogPost, Category


class BlogView(generic.ListView):
    template_name = 'web/blog.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

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
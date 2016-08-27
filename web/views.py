from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.utils import timezone
from django.views import generic

# Create your views here.
from django.views.generic import DetailView

from web.models import Me, BlogPost, Category


class BlogView(generic.ListView):
    template_name = 'web/blog.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['me'] = Me.objects.all()[0]
        return context

class BlogCategoryView(generic.ListView):
    template_name = 'web/blog.html'
    context_object_name = 'blog_posts'

    def get_queryset(self):
        category = self.kwargs['category'].replace('-', ' ')
        get_object_or_404(Category, name=category)
        return BlogPost.objects.filter(category__name=category)

    def get_context_data(self, **kwargs):
        context = super(BlogCategoryView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.kwargs['category'].replace('-', " ")
        return context

class BlogSingleView(DetailView):
    context_object_name = 'post'
    model = BlogPost
    template_name = 'web/blog-single.html'

def index(request):
    me = Me.get_solo()
    return render(request, 'web/index.html', { 'me':me })

def blog(request):
    return render(request, 'web/blog.html')

def portfolio(request):
    return render(request, 'web/portfolio.html')

def contact(request):
    return render(request, 'web/contact.html')


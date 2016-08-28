import json

from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.core.mail import send_mail

from .forms import ContactForm

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
        return BlogPost.objects.filter(categories__name=category)

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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("postik")
        if form.is_valid():
            print("juchu")
            subject = 'Message from personal webpage.'
            sender = form.cleaned_data['email']
            message = 'Name: ' + form.cleaned_data['name'] + "\n"+\
                      'Phone: ' + form.cleaned_data['phone'] + "\n"+ \
                      form.cleaned_data['message']
            recipients = [me.email]
            print("form data: "+form.cleaned_data['message'])
            send_mail(subject, message, sender, recipients)
            return HttpResponse(
                json.dumps({'state': 'ok'}), content_type='application/json'
            )
    else:
        form = ContactForm()
    print("tudlenudle")
    return render(request, 'web/index.html', { 'me':me, 'form':form })

def blog(request):
    return render(request, 'web/blog.html')

def portfolio(request):
    return render(request, 'web/portfolio.html')

def contact(request):
    return render(request, 'web/contact.html')


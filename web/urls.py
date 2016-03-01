from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.blog_single, name='blog_single'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
]
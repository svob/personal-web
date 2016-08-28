from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/', views.BlogSingleView.as_view(), name='blog_single'),
    url(r'^blog/category/(?P<category>.*)/$', views.BlogCategoryView.as_view(), name='blog_category'),
    url(r'^portfolio/$', views.PortfolioView.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<pk>[0-9]+)/', views.PortfolioSingleView.as_view(), name='portfolio_single'),
    url(r'^portfolio/category/(?P<category>.*)/$', views.PortfolioCategoryView.as_view(), name='portfolio_category'),
    url(r'^contact/$', views.contact, name='contact'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""AriasRoofingSiteProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from customers.views import *
from solid_i18n.urls import solid_i18n_patterns
from django.contrib.auth import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = solid_i18n_patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': Login}, name='login'),
    url(r'^landing/', Landing, name='landing'),
    url(r'^whyus/', WhyUsPage.as_view(), name='why us'),
    url(r'^about/', ContactPage.as_view(), name='about'),
    url(r'^services/', ServicesPage.as_view(), name='services'),
    url(r'^portfolio/', PortfolioPage.as_view(), name='portfolio'),
    url(r'^contact/', ContactPage.as_view(), name='contact'),
    url(r'^signup/', Signup, name='signup'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^', include('customers.urls')),
)

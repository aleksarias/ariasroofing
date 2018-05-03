from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'logout', 'login', 'why us', 'about', 'services', 'portfolio', 'contact', 'signup',]

    def location(self, item):
        return reverse(item)
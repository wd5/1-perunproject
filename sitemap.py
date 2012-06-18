from django.contrib.sitemaps import Sitemap
#from djangobb_forum.models import Forum, Topic
from simplepages.models import Page

class SitemapPage(Sitemap):
    priority = 0.8

    def items(self):
        return Page.objects.all()


class SitemapForum(Sitemap):
    priority = 0.5

    def items(self):
        return Forum.objects.all()


class SitemapTopic(Sitemap):
    priority = 0.5

    def items(self):
        return Topic.objects.all()

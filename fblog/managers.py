from django.db.models import Manager
import datetime


class PublicManager(Manager):
    """Returns published posts that are not in the future."""

    def published(self):
        return self.get_query_set().filter(is_published=True, date__lte=datetime.datetime.now())

    def visible(self):
        return self.get_query_set().filter(is_published=True, date__lte=datetime.datetime.now(), type__hidden_related=False)


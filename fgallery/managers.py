from django.db.models import Manager


class PublicManager(Manager):
    """Returns published items that are not in the future."""

    def published(self):
        return self.get_query_set().filter(is_published=True)

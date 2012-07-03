from selectable.base import ModelLookup
from selectable.registry import registry

from fblog.models import Ptype


class CategoryLookup(ModelLookup):
    model = Ptype
    search_fields = ('title__icontains', )

registry.register(CategoryLookup)

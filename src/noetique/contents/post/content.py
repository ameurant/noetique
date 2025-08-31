from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IPost(model.Schema):
    """Post schema"""

    # fields
    date = schema.Date(title="Date du post", required=True)


@implementer(IPost)
class Post(Item):
    """Post content type"""

    @property
    def title(self):
        computed_title = f"Le {self.date}"
        return computed_title

    @title.setter
    def title(self, value):
        pass

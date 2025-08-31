import datetime

from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IPost(model.Schema):
    """Post schema"""

    # fields
    effective = schema.Datetime(
        title="Moment du post",
        required=True,
        defaultFactory=lambda: datetime.datetime.now(),
    )


@implementer(IPost)
class Post(Item):
    """Post content type"""

    @property
    def title(self):
        computed_title = f"{self.effective.strftime('%A %d %B %Y')} à {self.effective.strftime('%HH%M')}"
        return computed_title

    @title.setter
    def title(self, value):
        pass

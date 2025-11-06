import datetime
import re

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
        # computed_title = f"{self.effective.strftime('%A %d %B %Y')} à {self.effective.strftime('%HH%M')}"
        computed_title = f"{self.effective.strftime('%A %d %B %Y')}"
        return computed_title.capitalize()

    @title.setter
    def title(self, value):
        pass

    @property
    def description(self):
        if self.text is None:
            return ""
        beginning = self.text.output[:300]
        clean_text = re.sub(r"<[^>]+>", "", beginning)
        return clean_text[:250] + "..."

    @description.setter
    def description(self, value):
        pass

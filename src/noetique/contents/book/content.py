from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IBook(model.Schema):
    """Book schema"""

    # fields
    title = schema.TextLine(title="Titre du livre", required=True)
    author = schema.TextLine(
        title="Auteur(s)",
        default="Marc Halévy",
        required=False,
    )
    description = schema.Text(
        title="Présentation du livre",
        required=True,
    )
    audience = schema.TextLine(
        title="Public",
        required=False,
    )
    cover = NamedBlobImage(
        title="Photo de couverture",
        required=False,
    )
    summary = RichText(
        title="Résumé détaillé du livre",
        required=False,
    )
    foreword = RichText(
        title="Préface du livre",
        required=False,
    )
    book = NamedBlobFile(
        title="Version gratuite du livre",
        required=False,
    )
    publisher = schema.TextLine(
        title="Editeur",
        required=False,
    )
    collection = schema.TextLine(
        title="Collection",
        required=False,
    )
    kind = schema.TextLine(
        title="Genre",
        required=False,
    )
    langue = schema.TextLine(
        title="Langue",
        required=False,
    )
    pages = schema.TextLine(
        title="Nombre de pages",
        required=False,
    )
    format = schema.TextLine(
        title="Format",
        required=False,
    )
    year = schema.TextLine(
        title="Année de publication",
        required=False,
    )
    isbn = schema.TextLine(
        title="ISBN",
        required=False,
    )

    # widgets
    directives.widget("description", rows=5)
    directives.widget("summary", rows=10)
    directives.widget("foreword", rows=10)

    # fieldsets
    model.fieldset(
        "metadata",
        label="Metadata",
        fields=["isbn", "publisher", "year", "format", "pages", "collection", "kind", "langue"],
    )


@implementer(IBook)
class Book(Item):
    """Book content type"""

import locale

from zope.i18nmessageid import MessageFactory

_ = MessageFactory("noetique")

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

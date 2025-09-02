from DateTime import DateTime
from plone import api
from Products.Five import BrowserView


class HomeView(BrowserView):
    @property
    def portal_path(self):
        portal = api.portal.get()
        return "/".join(portal.getPhysicalPath())

    @property
    def last_news(self):
        brains = api.content.find(
            portal_type="News Item",
            path=self.portal_path + "/actualites",
            review_state="published",
            sort_on="effective",
            sort_order="reverse",
            sort_limit=2,
        )

        items = []
        for b in brains[:2]:
            item = {
                "title": b.Title,
                "description": b.Description,
                "url": b.getURL() + "/view",
                "effective": b.effective.ISO(),
            }
            items.append(item)
        return items

    @property
    def last_articles(self):
        brains = api.content.find(
            portal_type=("Document", "File"),
            path=self.portal_path + "/billets",
            review_state="published",
            sort_on="effective",
            sort_order="reverse",
            sort_limit=3,
        )

        articles = []
        for b in brains[:3]:
            article = {
                "title": b.Title,
                "description": b.Description,
                "url": b.getURL() + "/view",
                "effective": b.effective.ISO(),
            }
            articles.append(article)
        return articles

    @property
    def last_thoughts(self):
        brains = api.content.find(
            portal_type="noetique.Post",
            # path=self.portal_path + "/journal",
            sort_on="effective",
            sort_order="reverse",
            sort_limit=3,
        )
        thoughts = []
        for b in brains[:3]:
            obj = b.getObject()
            thought = {
                "title": obj.title,
                "effective": obj.effective.isoformat(),
                "teaser": obj.text.output[:250],
                "url": obj.absolute_url() + "/view",
            }
            thoughts.append(thought)
        return thoughts

    @property
    def next_events(self):
        brains = api.content.find(
            portal_type="Event",
            path=self.portal_path + "/agenda",
            review_state="published",
            end={
                "query": [
                    DateTime(),
                ],
                "range": "min",
            },
            sort_on="start",
            sort_order="ascending",
        )
        events = []
        for b in brains[:3]:
            obj = b.getObject()
            event = {
                "title": b.Title,
                "description": b.Description,
                "start": b.start,
                "location": obj.location,
                "url": b.getURL(),
            }
            events.append(event)
        return events

    @property
    def last_books(self):
        brains = api.content.find(
            portal_type="noetique.Book",
            path=self.portal_path + "/livres",
            review_state="published",
            sort_on="effective",
            sort_order="reverse",
            sort_limit=4,
        )
        books = []
        for b in brains[:4]:
            obj = b.getObject()
            book = {
                "title": obj.title,
                "description": obj.description,
                "author": obj.author,
                "publisher": obj.publisher,
                "year": obj.year,
                "url": obj.absolute_url(),
            }
            books.append(book)
        return books

    @property
    def last_videos(self):
        brains = api.content.find(
            portal_type="Link",
            path=self.portal_path + "/videos",
            review_state="published",
            sort_on="effective",
            sort_order="reverse",
            sort_limit=3,
        )
        videos = []
        for b in brains[:3]:
            video = {
                "title": b.Title,
                "description": b.Description,
                "video_id": b.getRemoteUrl.split("?v=")[1] if "?v=" in b.getRemoteUrl else "",
            }
            if video["video_id"]:
                videos.append(video)
        return videos

class Article:
    instances = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.instances.append(self)

    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls.instances
    pass
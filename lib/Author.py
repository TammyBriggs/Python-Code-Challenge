class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
    pass
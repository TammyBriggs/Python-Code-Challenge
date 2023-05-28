class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles

    def magazines(self):
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine())
        return list(unique_magazines)

    def add_article(self, article):
        self._articles.append(article)
    
    pass
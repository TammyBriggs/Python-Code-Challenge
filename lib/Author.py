class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine

    def title(self):
        return self._title

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
            unique_magazines.add(article.magazine().name())
        return list(unique_magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
    
    def topic_areas(self):
        unique_categories = set()
        for article in self._articles:
            unique_categories.add(article.magazine().category())
        return list(unique_categories)

# Instances
# author = Author("Tammy Briggs")
# from Magazine import Magazine
# magazine1 = Magazine("Fendy", "Beauty")
# magazine2 = Magazine("Forbes", "Finance")

# author.add_article(magazine1, "Article 1")
# author.add_article(magazine2, "Article 2")
# author.add_article(magazine2, "Article 3")

# author_articles = author.articles()
# for article in author_articles:
#     print(article.title())
 
# author_magazines = author.magazines()   
# for magazine in author_magazines:
#     print(magazine2.name())

class Article:
    instances = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.instances.append(self)
        author.add_article(self, title)
        magazine.articles().append(self)

    def title(self):
        return self._title
    
    def author(self):
        return self._author.name

    def magazine(self):
        return self._magazine.name()

    @classmethod
    def all(cls):
        return cls.instances

# Instances
# from Author import Author
# author = Author("Tammy Briggs")
# from Magazine import Magazine
# magazine = Magazine("Fendy", "Beauty")

# article = Article(author, magazine, "Article 1")
# print(article.author())    
# print(article.magazine())  
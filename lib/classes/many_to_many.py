class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name


    def add_article(self, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set(magazine.category for magazine in magazines))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self._category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)

    def __repr__(self):
        return f"Article(author={self.author}, magazine={self.magazine}, title='{self.title}')"

class Article:
    all = []

    def __init__(self, author, magazine, title: str):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise ValueError("author must be an instance of Author and magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("new_author must be an instance of Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("new_magazine must be an instance of Magazine")
        self._magazine = new_magazine

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_article(article)

        return article

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None

class Magazine:
    def __init__(self, name: str, category: str):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("article must be an instance of Article")
        self._articles.append(article)
        

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributors(self):
        return list(set(article.author for article in self._articles))

    
    def contributors_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author not in author_counts:
                author_counts[author] = 0
            author_counts[author] += 1

        return [author for author, count in author_counts.items() if count > 2]

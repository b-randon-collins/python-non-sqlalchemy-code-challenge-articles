from article import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    
    @property
    def name(self):
        pass
    
    def articles(self):
        pass
    
    def magazines(self):
        pass
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
    
    def topic_areas(self):
        pass
'''
    app.util.testing
    ~~~~~~~~~~~~~~~~~
'''
import re
from random import randint
from faker import Faker
from app.extensions import db
from app.blog.models import BlogArticle, BlogCategory

fake = Faker()


def load_articles():
    a = []
    for article in BlogArticle.query.all():
        a.append(article)
    return a


def load_categories():
    c = []
    for category in BlogCategory.query.all():
        c.append(category)
    return c


def create_fake_articles(count=5):
    for _ in range(count):
        aname = fake.text(randint(25,50))
        fname = re.sub(r'\W+', '-', aname.lower())
        a = BlogArticle(article_name=aname, file_name=fname)
        a.commit()


def create_fake_categories(count=5):
    for _ in range(count):
        cname = fake.text(randint(5,10))
        c = BlogCategory(category_name=cname)
        c.commit()

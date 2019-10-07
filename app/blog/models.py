'''
    app.blog.models
    ~~~~~~~~~~~~~~~
'''
from app.extensions import db
from app.util.mixins import BaseModel, BaseControl

ac_assoc = db.Table(
    'blog_article_category_assoc',
    db.Column('article_id', db.Integer, db.ForeignKey('blog_article.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('blog_category.id'))
)


class BlogArticle(db.Model, BaseModel, BaseControl):
    article_name = db.Column(db.String(255), nullable=False, unique=True)
    file_name = db.Column(db.String(255), nullable=False, unique=True,
                          index=True)
    categories = db.relationship('BlogCategory',
                                 secondary=ac_assoc,
                                 backref=db.backref('articles',
                                                    lazy='dynamic'),
                                 lazy='dynamic')

    def __repr__(self):
        return '<Article {}>'.format(self.article_name)

    def has_category(self, category):
        return self.categories.\
            filter(ac_assoc.c.category_id == category.id).count() > 0

    def add_category(self, category):
        if not self.has_category(category):
            self.categories.append(category)

    def delete_category(self, category):
        if self.has_category(category):
            self.categories.remove(category)
        # Delete the category completely if the category doesn't have any
        # articles assigned to it.
        if not category.has_article():
            db.session.delete(category)


class BlogCategory(db.Model, BaseModel, BaseControl):
    category_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)

    def has_article(self):
        return self.articles.count() > 0

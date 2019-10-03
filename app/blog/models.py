'''
    app.blog.models
    ~~~~~~~~~~~~~~~
'''
from app.extensions import db
from app.base_models import BaseModel, BaseControl


article_category_assoc = db.Table(
    'blog_article_category_assoc',
    db.Column('article_id', db.Integer, db.ForeignKey('blog_article.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('blog_category.id'))
)


class BlogArticle(db.Model, BaseModel, BaseControl):
    article_name = db.Column(db.String(255), nullable=False, unique=True)
    file_name = db.Column(db.String(255), nullable=False, unique=True,
                          index=True)
    categories = db.relationship('BlogCategory',
                                 secondary=article_category_assoc,
                                 backref=db.backref('articles',
                                                    lazy='dynamic'),
                                 lazy='dynamic')

    def __repr__(self):
        return '<Article {}>'.format(self.article_name)


class BlogCategory(db.Model, BaseModel, BaseControl):
    category_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)

from flask_rest_jsonapi_next import ResourceList, ResourceDetail

from app import db
from app.models import Article
from app.schemas import ArticleSchema


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
from flask_rest_jsonapi_next import ResourceList, ResourceDetail

from app import db
from app.models import User
from app.schemas import UserSchema



class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
    }
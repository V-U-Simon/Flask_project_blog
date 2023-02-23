from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_view = 'user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'user_list'

    id = fields.Integer(as_string=True)
    username = fields.String(allow_none=False, required=True)
    email = fields.Email(allow_none=False, required=True)
    is_staff = fields.Boolean(allow_none=False)

    author = Relationship(
        nested='AuthorSchema',
        attribute='author',
        related_url='author_detail',
        related_url_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
    )
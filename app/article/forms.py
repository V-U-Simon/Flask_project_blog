from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, TextAreaField
from wtforms import validators



class ArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    body = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create')

   
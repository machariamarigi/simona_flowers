from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Products, Category


class ProductForm(FlaskForm):
    """Form for admin to add or edit a product"""

    name = StringField('Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    stock = StringField('Stock', validators=[DataRequired()])
    category = QuerySelectField(
        query_factory=lambda: Category.query.all(), get_label='name')
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    """Form for admin to add or edit a category"""

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    SubmitField = SubmitField('Submit')


class EventServiceForm(FlaskForm):
    """Form for admin to add or edit events and services"""

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    SubmitField = SubmitField('Submit')



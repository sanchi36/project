from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class getFoodForm(FlaskForm):
    image = StringField('Image Path',
                           validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Go Figure!')

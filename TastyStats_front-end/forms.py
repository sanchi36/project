from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from reader import getFoods

class getFoodForm(FlaskForm):
    image = StringField('Image Path',
                           validators=[DataRequired(), Length(min=5)])
    allFoods, uniqueFoods = getFoods()
    choices = []
    for i in range(len(uniqueFoods)):
        choices.append((uniqueFoods[i], uniqueFoods[i]))
    food = RadioField('Actual Label', choices=choices)
    submit = SubmitField('Go Figure!')

__author__ = 'deonheyns'
from flask.ext.wtf import Form
from wtforms import FloatField
from wtforms.validators import NumberRange, DataRequired


class PointsInRadiusForm(Form):
    latitude = FloatField('latitude', validators=[NumberRange(-999, 999), DataRequired()])
    longitude = FloatField('longitude', validators=[NumberRange(-999, 999), DataRequired()])
    radius = FloatField('radius', validators=[NumberRange(0, 4000), DataRequired()])
    num_of_points = FloatField('num_of_points', validators=[NumberRange(0, 360, "Range between 0 - 360"), DataRequired()])

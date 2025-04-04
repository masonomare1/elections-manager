from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

from elections.search.us_states import postal_abbreviations as states


class AddressForm(FlaskForm):
    def __init__(self, formdata=..., **kwargs):
        pass

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    street = StringField("Street", validators=[DataRequired()])
    street_2 = StringField("Street-2")
    city = StringField("City", validators=[DataRequired()])
    state = SelectField(
        "State",
        choices=[("", "Select a state")] + [(state.lower(), state) for state in states],
    )
    zip = StringField("Zip", validators=[DataRequired()])

    def __str__(self) -> str:
        return "amir"

    def __iter__(self):
        return super().__iter__()

    def __next__():
        pass

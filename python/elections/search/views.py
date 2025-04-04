from sys import excepthook
from flask import Blueprint, render_template, request

from elections.search.forms import AddressForm
from elections.search.us_states import postal_abbreviations
from elections.search.utils import generate_ocd_ids, get_upcoming_elections

search_router = Blueprint("address_form", __name__, url_prefix="/")


@search_router.route("/search", methods=("GET", "POST"))
@search_router.route("/")
def search():
    form = AddressForm()

    if request.method == "POST" and form.validate_on_submit():
        state_ocd_id, place_ocd_id = generate_ocd_ids(**form.data)
        elections = get_upcoming_elections(state_ocd_id, place_ocd_id)

        return render_template("election_results.html", elections=elections)

    return render_template("address_form.html", states=postal_abbreviations, form=form)

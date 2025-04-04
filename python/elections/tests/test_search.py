from elections.search.utils import generate_ocd_ids, get_upcoming_elections


class TestSearchAPI:
    def test_submit_address_form_with_valid_data(self, testapp):
        response = testapp.get("/")

        form = response.forms[0]
        form["street"] = "123 Main St"
        form["street_2"] = "123 Main St"
        form["city"] = "Gulfport"
        form["state"] = "ms"
        form["zip"] = "12345"

        response = form.submit()

        assert 200 == response.status_code
        assert "Description:" in response
        assert "Date:" in response
        assert "Type:" in response
        assert "Website:" in response

    def test_submit_address_form_with_invalid_data(self, testapp):
        response = testapp.get("/")

        form = response.forms[0]
        form["street_2"] = "123 Main St"
        form["city"] = "Gulfport"
        form["state"] = "ms"

        response = form.submit()

        assert 200 == response.status_code
        assert "Find my next election" in response
        assert "This field is required." in response


def test_ocd_id_generation():
    data = {"street": "123 Main St", "street_2": "123 Main St", "city": "Gulfport", "state": "ms", "zip": "12345"}

    state_ocd_id, place_ocd_id = generate_ocd_ids(**data)

    assert state_ocd_id == f"ocd-division/country:us/state:ms"
    assert place_ocd_id == f"ocd-division/country:us/state:ms/place:gulfport"


def test_get_upcoming_elections():
    state_ocd_id = "ocd-division/country:us/state:ms"
    place_ocd_id = "ocd-division/country:us/state:ms/place:gulfport"
    elections = get_upcoming_elections(state_ocd_id, place_ocd_id)

    for election in elections:
        assert election["district-divisions"][0]["ocd-id"] == state_ocd_id

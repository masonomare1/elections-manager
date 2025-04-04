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


if __name__ == "__main__":
    unittest.main()

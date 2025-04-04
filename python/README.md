# Elections Finder Web Application

The Elections Finder is a web application that allows users to find upcoming elections based on their address. The application uses the Democracy Works Elections API to fetch election data for the provided address.

## Getting Started

To run the Elections Finder web application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up the Flask application by exporting the necessary environment variables or using a `.env` file.
4. Start the application by running `flask --app autoapp.py run`.

The web application will be accessible at `http://localhost:5000`.

## How it Works

When a user visits the web application, they will be presented with an address form. Upon submitting the form, the application will translate the address into Open Civic Data division identifiers (OCD IDs) and query the Democracy Works Elections API for upcoming elections for those OCD IDs. The API will return election data, which will be displayed to the user.

## API Endpoints

### Search Endpoint

- **URL:** `/search`
- **Method:** POST
- **Parameters:**
  - `street` (string): The street address.
  - `street_2` (string, optional): Additional street address.
  - `city` (string): The city.
  - `state` (string): The state abbreviation (e.g., "NY" for New York).
  - `zip` (string): The ZIP code.
- **Response:** Returns the upcoming elections for the provided address.

## Project Structure

The project follows the following directory structure:
```
project-root/
|-- app.py # Flask application entry point
|-- forms.py # Flask forms definition
|-- templates/
| |-- address_form.html # HTML template for the address form
| |-- election_results.html # HTML template to display upcoming elections
|-- static/ # Directory for static assets (CSS, JS, etc.)
|-- tests/ # Directory containing test files
|-- README.md # Project documentation
|-- requirements.txt # Dependencies file
```


## Dependencies & New Tools Used

The Elections Finder web application uses the following main dependencies:

- Flask: A micro web framework for Python.
- Requests: A library for making HTTP requests.
- WebTest: A library for testing WSGI applications.
- Jinja2: A templating engine for Python.

## Testing

The project includes unit tests to ensure the functionality of the web application. To run the tests, use the following command:

```bash
pytest
```
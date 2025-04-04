from flask import Flask

from elections.search.views import search_router


def create_app(config_object="elections.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(search_router)

    return None

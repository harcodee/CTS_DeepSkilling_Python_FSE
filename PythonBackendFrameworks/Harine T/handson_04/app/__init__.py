from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes import courses_bp
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found(error):
        return {
            "status": "error",
            "message": "Resource not found"
        }, 404

    @app.errorhandler(400)
    def bad_request(error):
        return {
            "status": "error",
            "message": "Bad request"
        }, 400

    @app.errorhandler(500)
    def internal_server_error(error):
        return {
            "status": "error",
            "message": "Internal Server Error"
        }, 500

    return app
from flask import Flask
from config import Config
from courses.routes import courses_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprint
    app.register_blueprint(courses_bp)

    # JSON Error Handler - 404
    @app.errorhandler(404)
    def not_found(error):
        return {
            "status": "error",
            "message": "Resource not found"
        }, 404

    # JSON Error Handler - 500
    @app.errorhandler(500)
    def internal_server_error(error):
        return {
            "status": "error",
            "message": "Internal Server Error"
        }, 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
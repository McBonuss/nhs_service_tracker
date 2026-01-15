from flask import Flask, render_template
from dotenv import load_dotenv
from .extensions import db, migrate, login_manager, csrf
from .config import get_config
from .models import User
from .views.main import main_bp
from .views.auth import auth_bp
from .views.patients import patients_bp
from .views.services import services_bp
from .views.appointments import appointments_bp


def create_app(config_name=None):
    """Application factory.

    Ensures environment variables from the project-level "env" file are
    loaded even when the app is started directly via wsgi.py (not only
    through the Flask CLI). This keeps DATABASE_URL and SECRET_KEY
    consistent with what setup.ps1 configures.
    """

    # Load variables from the local env file if present; this is a no-op
    # when the file is missing or when values are already set in os.environ.
    load_dotenv("env")

    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(patients_bp, url_prefix="/patients")
    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(appointments_bp, url_prefix="/appointments")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("500.html"), 500

    return app

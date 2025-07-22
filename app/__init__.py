from flask import Flask
from app.extensions import db
from app.blueprints.public.routes import public_bp  # ✅ Import public blueprint

def create_app():
    app = Flask(__name__, template_folder='templates')

    # ✅ Load configuration
    app.config.from_object('app.config.Config')

    # ✅ Initialize extensions
    db.init_app(app)

    # ✅ Register blueprints
    app.register_blueprint(public_bp)

    return app

from flask import Flask
from public.routes import public_bp

app = Flask(__name__)
app.register_blueprint(public_bp)

if __name__ == '__main__':
    app.run(debug=True)

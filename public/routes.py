from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__, template_folder='templates', static_folder='static')

@public_bp.route('/')
def index():
    return render_template('public/index.html')

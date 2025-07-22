from flask import Blueprint, render_template

# ✅ Create the blueprint object
public_bp = Blueprint(
    'public',
    __name__,
    template_folder='../../templates/public'  # 👈 make sure this path is correct
)

# ✅ Homepage route
@public_bp.route('/')
def home():
    return render_template('public/home.html')  # 👈 this should exist

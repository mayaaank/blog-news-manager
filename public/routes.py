from flask import Blueprint, render_template

public_bp = Blueprint('public', __name__, template_folder='templates', static_folder='static')

@public_bp.route('/')
def public_home():
    posts = [
        {
            'title': 'Welcome to the Blog!',
            'content': 'This is a short introduction to the blog. We cover tech, programming, and more.',
            'author': 'Admin',
            'date': 'July 17, 2025'
        },
        {
            'title': 'Getting Started with Flask',
            'content': 'Flask is a micro web framework for Python. It’s simple and easy to get started with.',
            'author': 'Mayank',
            'date': 'July 16, 2025'
        }
    ]
    return render_template('public/index.html', posts=posts)

# app/home/routes.py

from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/api/posts')
def get_posts():
    # Dummy data for testing frontend
    return jsonify([
        {"id": 1, "title": "First Blog", "author": "Mayank", "desc": "Intro to Civora Blog"},
        {"id": 2, "title": "React Integration", "author": "Team", "desc": "Frontend is live"},
        {"id": 3, "title": "PostgreSQL Setup", "author": "You", "desc": "Database connected"},
    ])

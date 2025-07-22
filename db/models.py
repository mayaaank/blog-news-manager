# db/models.py

from flask_sqlalchemy import SQLAlchemy

# 🧠 This will be initialized in your main __init__.py (app factory)
db = SQLAlchemy()


# ✅ Blog post model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

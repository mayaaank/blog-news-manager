# 📝 Fullstack Blog Website

A fullstack blog application built with **React + Vite (frontend)** and **Flask + PostgreSQL (backend)**. The goal is to create a modern, responsive blog platform with categories, search, user management, and admin control.

---

## 📦 Tech Stack

### Frontend
- ⚛️ React (with Vite)
- 🎨 Plain CSS (themed: Tech-style / Neumorphic UI)
- 📱 Responsive Design (Hero Section, Cards, Sticky Navbar)

### Backend
- 🐍 Flask (Python)
- 🐘 PostgreSQL (via SQLAlchemy)
- 🔐 Environment-based config (`.env`)
- 🧠 Jinja2 templates for SSR

---

## 📁 Folder Structure
```
├── app/ # Flask application (routes, templates)
├── db/ # Database models (PostgreSQL + SQLAlchemy)
├── frontend/ # React + Vite frontend (separate dev server)
├── migrations/ # Flask-Migrate history
├── .gitignore # Files ignored by Git
├── run.py # Entry point for Flask backend
└── requirements.txt # Python dependencies
```
## 🚀 How to Run Locally
# Create virtual environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

# Install dependencies 
```
pip install -r requirements.txt
```
# Setup DB
```
flask db init
flask db migrate -m "initial"
flask db upgrade
```
# Run backend
```
python run.py
```

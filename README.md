# Civora Blog Manager 📝

A  blog management system built with **Flask** and **PostgreSQL**, supporting both **admin control panel** and a **public-facing blog page**. 

---

## 🔧 Tech Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Vanilla), Jinja2 Templating
- **Version Control**: Git

---

## 🗂️ Project Structure

blog-manager/
├── public/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── public/
│   │       └── index.html
│   ├── __pycache__/
│   │   ├── routes.cpython-313.pyc
│   │   └── __init__.cpython-313.pyc
│   ├── routes.py
│   └── __init__.py
├── templates/
│   └── base.html
├── app.py
├── requirements.txt
├── README.md
└── .gitignore



## 🛠️ Setup Instructions

## ⚙️ Setup Instructions
## ⚙️ Setup Instructions

1. **Create virtual environment & activate**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate


2.Install dependencies
pip install -r requirements.txt

3.Run the Flask app
python app.py

4.Visit in browser
http://127.0.0.1:5000
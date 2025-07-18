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

📦blog-manager/
┣ 📂admin/ → Admin routes & templates
┃ ┣ 📜__init__.py
┃ ┣ 📜routes.py
┃ ┗ 📂templates/admin/
┃ ┣ create.html
┃ ┣ dashboard.html
┃ ┣ edit.html
┃ ┗ login.html
┣ 📂public/ → Public routes & templates
┃ ┣ 📜__init__.py
┃ ┣ 📜routes.py
┃ ┣ 📂static/css/
┃ ┃ ┗ style.css
┃ ┗ 📂templates/public/
┃ ┗ index.html
┣ 📂templates/
┃ ┗ base.html → Common base template
┣ 📜app.py
┗ 📜README.md → This file

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/mayaaank/blog-news-manager.git
   cd blog-news-manager
Create & activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure PostgreSQL and environment variables

Run the app

bash
Copy
Edit
python app.py

# Maternal Health App

A backend system for tracking maternal health data. Built with FastAPI and SQLite, this app allows healthcare workers or family caregivers to record and monitor essential information for mothers during pregnancy and postpartum.

#  🚀 Features

Add and store maternal health records (e.g., name, age, medical notes).

Lightweight database using SQLite.

API endpoints built with FastAPI.

Easy to run locally and extendable for future AI/ML features.

# 📂 Project Structure
maternal-app/
│── main.py          # FastAPI entry point
│── db.py            # Database setup with SQLAlchemy
│── models.py        # Data models
│── requirements.txt # Python dependencies
│── README.md        # Project documentation

# ⚙️ Installation

Clone this repository:

git clone https://github.com/attohx/maternal_app.git
cd maternal_app


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt

# ▶️ Usage

Run the app:

uvicorn main:app --reload


Go to your browser:
👉 http://127.0.0.1:8000/docs

Here you can test all the API endpoints in an interactive UI.

# 🗂 Database

The app uses SQLite by default. A database file called maternal_health.db will be created automatically when you run the app.
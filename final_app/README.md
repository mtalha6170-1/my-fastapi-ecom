# 🛒 E-Commerce API (FastAPI)

This is a simple and powerful E-commerce API built using FastAPI and SQLite.It includes CRUD operations to efficiently manage Products and Orders.

## 🚀 Features
* **Fast & Lightweight**: Built with FastAPI.
* **Database:** SQLite (using SQLAlchemy ORM).
* **Schemas:** Pydantic models for data validation.
* **Documentation:** Interactive Swagger UI automatically generated.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database:** SQLite
* **Server:** Uvicorn

## 📂 Project Structure
```text
final_app/
├── main.py        # API Routes & App Initialization
├── models.py      # Database Tables (SQLAlchemy)
├── schemas.py     # Data Validation (Pydantic)
├── database.py    # Connection Setup
└── crud.py        # Create, Read, Update, Delete Logic

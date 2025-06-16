# 📞 FastAPI Contact Manager

A lightweight FastAPI application to manage contacts using SQLAlchemy ORM and PostgreSQL. This project demonstrates creating, retrieving, and deleting contact records with full Pydantic validation and asynchronous API handling.

---

## 🚀 Features

- 🔁 RESTful API with FastAPI
- 🗃️ PostgreSQL database with SQLAlchemy ORM
- 📦 Pydantic models for schema validation
- ♻️ Async support for improved performance
- ✅ Dependency Injection for clean DB session management

---

## 🛠️ Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for PostgreSQL
- **Pydantic** - Data validation
- **PostgreSQL** - Relational database
- **Uvicorn** - Swagger Ui / ASGI server



---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/atharvarakshak/fastapi-docker-app.git
cd fastapi-docker-app
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL through docker
Ensure you have a PostgreSQL database running and update your SQLALCHEMY_DATABASE_URL in database.py:
```bash
 scripts/postgres.sh

 SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```


### 5. Run the application
```bash
uvicorn main:app --reload
```

---
🔌 API Endpoints
- POST /api/contacts/ – Create a contact

- GET /api/contacts/ – Get all contacts

- GET /api/contacts/{id}/ – Get a single contact

- DELETE /api/delete/{id}/ – Delete a contact
---

✅ To-Do
- Add update contact functionality

- Write unit tests with pytest

- Setup yml file

- Dockerize the application


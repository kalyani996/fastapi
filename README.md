# 📝 FastAPI Blog & User Management API

A lightweight, secure RESTful API built with **FastAPI**, featuring full CRUD operations for blogs and users, JWT-based authentication, and SQLAlchemy ORM. 
This project is designed for learning, experimentation, and as a foundation for more complex backend systems.

## 🚀 Live Demo

Check out the deployed version on Render:  
👉 [https://fastapi-1-fvk0.onrender.com/docs](https://fastapi-1-fvk0.onrender.com/docs) *(Swagger UI)*

## 🔧 Features

- ✅ CRUD for Blog Posts and Users
- 🔐 JWT Authentication for secure access
- 🧰 SQLAlchemy for ORM-based data management
- 🧪 Pydantic for request/response validation
- ⚙️ Dependency Injection and modular route structure
- 💾 SQLite database (easy to replace with PostgreSQL or others)
- 📄 Auto-generated interactive API docs (Swagger/OpenAPI)

## 🧪 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Pydantic](https://docs.pydantic.dev/)  
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)  
- [Render](https://render.com/) (deployment platform)

## 🔐 Authentication

The API uses **JWT tokens** for user authentication. To test:
1. Register a new user via `/user`
2. Login via `/login` to receive a token
3. Use the token in the "Authorize" button on Swagger to access protected endpoints

## 🛠️ Installation

```bash
git clone https://github.com/kalyani996/fastapi.git
cd fastapi
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn blog.main:app --reload

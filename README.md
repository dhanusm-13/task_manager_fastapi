# 📝 Task Manager API

A high-performance REST API built with **FastAPI** and **SQLAlchemy** to manage daily tasks. This project features a persistent SQLite database, query optimization through filtering/pagination, and is fully deployed to a cloud environment.

## 🔗 Live Demo

🚀 **View Live API:** https://task-manager-ndt0.onrender.com/

📖 **Interactive Docs:** https://task-manager-ndt0.onrender.com/docs

## 🚀 Features

* **Full CRUD Operations**: Seamlessly create, read, update, and delete tasks.
* **Advanced Querying**: Search for tasks by title and filter by completion status using query parameters.
* **Pagination**: Optimized data retrieval using `skip` and `limit` to handle large datasets efficiently.
* **Database Persistence**: Integrated **SQLite** via **SQLAlchemy ORM** to ensure data survives server restarts.
* **Automatic Documentation**: Instant, interactive API docs generated via Swagger UI and ReDoc.
* **Production Ready**: Configured for deployment with Gunicorn/Uvicorn and production-grade environment settings.

## 🛠️ Tech Stack

* **FastAPI**: Modern, fast web framework for building APIs with Python 3.8+.
* **SQLAlchemy**: Powerful SQL Toolkit and Object-Relational Mapper (ORM).
* **SQLite**: Lightweight, serverless database engine for persistent storage.
* **Pydantic**: Data validation and settings management using Python type annotations.
* **Render**: Cloud platform used for hosting the live web service.

## 📦 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/dhanusm-13/task_manager_fastapi.git
cd task_manager_fastapi

```


2. **Create a virtual environment**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

```


3. **Install dependencies**
```bash
pip install -r requirements.txt

```



## 🏃 How to Run Locally

Start the development server:

```bash
uvicorn main:app --reload

```

The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 📡 Key Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| **GET** | `/tasks` | List tasks (Supports `?title=`, `?completed=`, `?skip=`, `?limit=`) |
| **GET** | `/tasks/{id}` | Get detailed information for a specific task |
| **POST** | `/tasks` | Create a new task |
| **PUT** | `/tasks/{id}` | Update task title, description, or status |
| **DELETE** | `/tasks/{id}` | Permanently remove a task from the database |

---

## 👤 Author

**Dhananjaya S M**

* GitHub: [@dhanusm-13](https://www.google.com/search?q=https://github.com/dhanusm-13)
* LikedIn:[dhananjayasm](https://www.linkedin.com/in/dhananjaya-s-m/)

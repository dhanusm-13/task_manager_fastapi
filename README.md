# 📝 Task Manager API

A high-performance REST API built with **FastAPI** and **SQLAlchemy** to manage daily tasks. This project features a persistent SQLite database and automatic documentation.

## 🚀 Features
- **Full CRUD**: Create, Read, Update, and Delete tasks  
- **Database Persistence**: Uses SQLite to keep your tasks saved  
- **Automatic Docs**: Interactive API documentation via Swagger UI  
- **Data Validation**: Powered by Pydantic models  

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework  
- [SQLAlchemy](https://www.sqlalchemy.org/) – SQL Toolkit and ORM  
- [SQLite](https://www.sqlite.org/) – Database engine  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/dhanusm-13/task_manager_fastapi.git](https://github.com/dhanusm-13/task_manager_fastapi.git)
   cd task_manager_fastapi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

## 🏃 How to Run

Start the server using Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📖 API Documentation

Once the server is running, you can access interactive docs:  
- Swagger UI → `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")  
- ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

## 📡 Endpoints

| Method | Endpoint       | Description                     |
|--------|----------------|---------------------------------|
| GET    | `/`            | Root greeting                   |
| GET    | `/tasks`       | Retrieve all tasks              |
| GET    | `/tasks/{id}`  | Retrieve a specific task by ID  |
| POST   | `/tasks`       | Create a new task               |
| PUT    | `/tasks/{id}`  | Update an existing task         |
| DELETE | `/tasks/{id}`  | Remove a task                   |

---

## 👤 Author

**Dhananjaya S M**  


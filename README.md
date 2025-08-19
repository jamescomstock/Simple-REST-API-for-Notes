# 📝 Simple Notes REST API (FastAPI)

A **simple and secure REST API** for managing notes, built with **FastAPI**.  
Supports **CRUD operations** (Create, Read, Update, Delete) and **API Key authentication**.

---

## ✅ Features
- **Fast and modern API** using [FastAPI](https://fastapi.tiangolo.com/)
- **CRUD endpoints** for notes:
  - Create a new note
  - List all notes
  - Retrieve a single note
  - Update a note
  - Delete a note
- **API Key authentication** for all endpoints
- Interactive API docs at `/docs`

---

## 📂 Project Structure
```
notes_api/
├── main.py # Main FastAPI app
├── models.py # Pydantic models for request/response
├── database.py # In-memory storage and ID generator
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

🛠 Example Usage
Create a Note

```bash
curl -X POST "http://127.0.0.1:8000/notes" \
-H "Content-Type: application/json" \
-H "x-api-key: supersecretapikey" \
-d '{"title":"My First Note","content":"Hello FastAPI!"}'
```

Get All Notes
```bash
curl -X GET "http://127.0.0.1:8000/notes" \
-H "x-api-key: supersecretapikey"
```

# crud-fastAPI

Simple and efficient CRUD API for task management built with FastAPI, SQLAlchemy, and Docker.

## Features
- ✅ Full CRUD Operations (Create, Read, Update, Delete)
- 🔔 Email notifications on task creation (background processing)
- 🎚 Filter tasks by completion status
- 📏 Pagination support
- 🐳 Docker containerization
- 📊 Automatic API documentation via Swagger UI

## Technology Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PosgreSQL
- **Server**: Uvicorn
- **Containerization**: Docker
- **Validation**: Pydantic

## API Endpoints
| Method | Endpoint         | Description                     |
|--------|------------------|---------------------------------|
| POST   | `/api/v1/tasks`  | Create new task                 |
| GET    | `/api/v1/tasks`  | List all tasks (filterable)     |
| PUT    | `/api/v1/tasks/{id}` | Update existing task        |
| DELETE | `/api/v1/tasks/{id}` | Delete task                 |

## Setup & Installation

### Local Environment
```bash
# Clone repository
git clone https://github.com/yourusername/crud-fastapi.git
cd crud-fastapi

# Install dependencies (recommended: Python 3.8+)
pip install -r requirements.txt

# Start application
uvicorn main:app --reload
```

### Docker
```bash
# Build and start containers
docker-compose up --build

# Access API at http://localhost:8088
```

## API Documentation
After starting the server, access the interactive documentation:
- Swagger UI: http://localhost:8088/docs
- ReDoc: http://localhost:8088/redoc

## Directory Structure
```
crud-fastapi/
├── backend/
│   ├── db/            # Database configuration
│   ├── handlers/      # API controllers
│   ├── models/        # Schemas and DB models
│   └── services/      # Business logic
├── docker-compose.yaml
├── main.py            # Application entrypoint
├── requirements.txt   # Dependencies
└── README.md
```

## Contributing
Contributions are welcome! Please fork the repository and open a pull request.

## License
[MIT License](LICENSE)
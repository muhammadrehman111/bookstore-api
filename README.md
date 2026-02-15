# BookStore API

A simple REST API for managing a bookstore, built with Flask and SQLAlchemy.

## Features

- **GET** all books
- **POST** new books
- SQLite database by default (configurable to PostgreSQL)
- Comprehensive test suite with pytest
- Docker support for containerized deployment
- CI/CD pipeline with GitHub Actions

## Prerequisites

- Python 3.11+ (3.12+ recommended)
- pip or conda
- Docker (optional, for containerized deployment)
- Git

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/muhammadrehman111/bookstore-api.git
cd bookstore-api
```

### 2. Create virtual environment
```bash
python -m venv .venv
```

### 3. Activate virtual environment

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
.venv\Scripts\python app.py
```

Or using Flask CLI:
```bash
.venv\Scripts\python -m flask --app app run
```

The API will be available at `http://localhost:5000`

### Using Docker

Build the image:
```bash
docker build -t bookstore-api .
```

Run the container:
```bash
docker run -p 5000:5000 bookstore-api
```

## API Endpoints

### 1. Welcome
```
GET /
```
Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to BookStore API"
}
```

### 2. Get All Books
```
GET /books
```
Retrieve all books from the database.

**Response:**
```json
[
  {
    "id": 1,
    "title": "DevOps Fundamentals"
  },
  {
    "id": 2,
    "title": "Mastering CI/CD"
  },
  {
    "id": 3,
    "title": "Flask for Beginners"
  }
]
```

### 3. Add New Book
```
POST /books
```
Add a new book to the database.

**Request Body:**
```json
{
  "title": "Your Book Title"
}
```

**Response:**
```json
{
  "message": "Book added successfully"
}
```

## Running Tests

```bash
.venv\Scripts\python -m pytest -q
```

Or with verbose output:
```bash
.venv\Scripts\python -m pytest -v
```

## Database Configuration

By default, the app uses **SQLite** (`books.db` in the project root).

To use PostgreSQL, set the environment variable before running:

```bash
$env:DATABASE_URL="postgresql://user:password@localhost:5432/bookstore"
.venv\Scripts\python app.py
```

## Directory Structure

```
bookstore-api/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions CI/CD pipeline
├── tests/
│   └── test_app.py       # Test suite
└── instance/             # Flask instance folder (auto-created)
```

## Development Notes

- The database is auto-created on first run
- Sample books are seeded automatically on initial setup
- Modify `requirements.txt` if you need additional packages (e.g., psycopg2 for PostgreSQL)

## CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/ci-cd.yml`) that:
1. Runs on every push to `main` branch
2. Sets up Python 3.11 environment
3. Installs dependencies
4. Executes all tests
5. Builds and pushes Docker image to Docker Hub (requires secrets configured)

### Setting up Secrets

Configure these GitHub repository secrets for Docker deployment:
- `DOCKER_USERNAME` – Your Docker Hub username
- `DOCKER_PASSWORD` – Your Docker Hub access token

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, open a GitHub issue or contact the maintainers.

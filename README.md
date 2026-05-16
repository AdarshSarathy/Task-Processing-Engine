# FastAPI Task Processing Engine 🚀

A highly optimized, type-safe RESTful API for tracking and processing tasks, engineered using modern Python practices.

This repository serves as a showcase of clean backend architecture, robust database management, and extensive testing integration suitable for enterprise-level Python applications.

## ✨ Key Features

- **Modern API Architecture**: Built entirely on [FastAPI](https://fastapi.tiangolo.com/), utilizing its blistering fast capabilities.
- **Relational Database Management**: Uses **SQLite** integrated via **SQLAlchemy** (ORM) for clean, reliable data persistence and transactions.
- **Strict Data Validation**: Leverages **Pydantic** models to actively ensure type safety, request validation, and clean data serialization.
- **Automated Open Documentation**: Natively generates interactive, standards-compliant OpenAPI/Swagger UI endpoints out of the box to share knowledge effectively.
- **Test-Driven Design**: Extensively covered by a **Pytest** integration test suite that utilizes completely isolated test-databases.
- **Clean Code**: Code is highly maintainable, formatted cohesively, and rigorously typed in absolute alignment with standard PEP-8 Python development guidelines.

## 🛠️ Technology Stack

- **Python**: 3.9+
- **Framework**: FastAPI
- **Server**: Uvicorn
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing**: Pytest & HTTPX

## 🚀 Getting Started

Follow these steps to initialize and run the local development server.

### Prerequisites

- Python 3.9 or higher

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd python-portfolio-api
   ```

2. **Setup a isolated virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install exact dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the local server:**
   ```bash
   uvicorn main:app --reload
   ```

## 📖 Usage & Documentation

Once the server is efficiently running on `http://localhost:8000`, the powerful REST endpoints dynamically await any requests.

### Interactive API Documentation

FastAPI automatically generates heavily comprehensive documentation. Simply navigate your local browser to:
- **[Swagger UI Playground](http://localhost:8000/docs)** to actively test parameters and responses.
- **[ReDoc Format](http://localhost:8000/redoc)** for alternative structured documentation layout.

### Running Automated Tests

To consistently verify backend integrity locally across continuous developments, launch the unified testing suite using:
```bash
pytest
```
The Pytest suite runs automatically against its own test fixtures without ever touching your primary database file!

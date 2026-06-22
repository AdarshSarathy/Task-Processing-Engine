# FastAPI Task Processing Engine 🚀

A highly optimized, type-safe RESTful API for tracking and managing asynchronous task lifecycles, engineered using modern Python backend practices.

This repository serves as a showcase of clean backend architecture, robust database management, transaction safety, and production-ready asynchronous API routing suitable for enterprise-level applications.

## ✨ Key Features

- **Asynchronous API Architecture**: Built entirely on **FastAPI**, leveraging its native asynchronous routing to concurrently handle long-running task lifecycles with minimal latency.
- **Relational Database Management**: Utilizes **SQLAlchemy (ORM)** to manage clean data persistence, enforcing transaction safety and data integrity through isolated database engine pools.
- **Strict Data Validation & Serialization**: Leverages **Pydantic** models to actively guarantee compile-time type safety, strict request validation, and explicit data serialization.
- **Automated OpenAPI Documentation**: Natively generates interactive, standards-compliant OpenAPI/Swagger UI endpoints out of the box to expose clean, self-documenting services.
- **Robust Error Handling**: Implements clean relational data modeling to catch database anomalies gracefully and deliver structured, meaningful JSON error responses to the client.
- **Clean Code Practices**: Cohesively formatted and rigorously typed in absolute alignment with standard PEP-8 Python development guidelines for high maintainability.

## 🛠️ Technology Stack

- **Python**: 3.9+
- **Framework**: FastAPI
- **Server**: Uvicorn
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Database**: SQLite (Configured with isolated connection pools)

## 🚀 Getting Started

Follow these steps to initialize and run the local development server.

### Prerequisites

- Python 3.9 or higher

### Installation

1. **Clone the repository:**
   `git clone https://github.com/AdarshSarathy/Task-Processing-Engine.git`
   `cd python-portfolio-api`

2. **Setup an isolated virtual environment:**
   `python -m venv venv`
   **On Windows:**
   `.\venv\Scripts\activate`
   **On macOS/Linux:**
   `source venv/bin/activate`

3. **Install exact dependencies:**
   `pip install -r requirements.txt`

4. **Run the local server:**
   `uvicorn main:app --reload`

## 📖 Usage & Documentation

Once the server is running on `http://localhost:8000`, the REST endpoints dynamically await requests.

### Interactive API Documentation

FastAPI automatically analyzes your routing and schemas to generate comprehensive interactive documentation. Navigate your local browser to:
- **Swagger UI Playground** (`http://localhost:8000/docs`) to actively test parameters, headers, and payloads directly from the browser.
- **ReDoc Format** (`http://localhost:8000/redoc`) for an alternative, highly structured documentation layout optimized for deep schema inspection.

# Fast API Learning

## Standard Production-Ready Structure
#### For most scalable applications, use a structure similar to this:
├── app/<br>
│   ├── __init__.py<br>
│   ├── main.py              # App entry point & router inclusion<br>
│   ├── core/                # Global config (settings, security, etc.)<br>
│   ├── db/                  # Database session & engine setup<br>
│   ├── models/              # Database models (e.g., SQLAlchemy/SQLModel)<br>
│   ├── schemas/             # Pydantic models for request/response validation<br>
│   ├── routers/             # API endpoint definitions (using APIRouter)<br>
│   ├── services/            # Business logic (kept separate from routes)<br>
│   └── dependencies.py      # Shared dependencies (e.g., get_db, auth)<br>
├── tests/                   # Unit and integration tests<br>
├── .env                     # Environment variables<br>
├── requirements.txt         # Project dependencies<br>
└── alembic/                 # Database migrations (optional but recommended)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file will be created in the backend/ directory
# Path is relative to where you run uvicorn (i.e., the nutritrack/ folder)
SQLALCHEMY_DATABASE_URL = "sqlite:///./backend/db.sqlite"

# Important for SQLite with multiple connections (like FastAPI + reload)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite in threaded environments
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
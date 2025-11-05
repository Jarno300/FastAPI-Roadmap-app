from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import users
from app.db.base import Base
from app.db.session import engine, SessionLocal

app = FastAPI(title = "Roadmap API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router, prefix="/users", tags=["users"])


# Ensure tables exist on startup (use Alembic in production for migrations)
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    # Place for shutdown code if needed


@app.get("/", tags=["meta"])
def root():
    return {"name": "Roadmap API", "version": "1.0.0"}


@app.get("/health", tags=["meta"])
def health():
    # Simple DB check
    try:
        with SessionLocal() as db:
            db.execute("SELECT 1")
        db_ok = True
    except Exception:
        db_ok = False
    return {"status": "ok", "db": db_ok}


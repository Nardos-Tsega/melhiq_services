from app.db.base import Base

class Session(Base):
    __tablename__ = "sessions"

    id: int
    user_id: int
    session_token: str
    is_active: bool
    created_at: str
    updated_at: str
from app.db.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: int
    user_id: int
    token: str
    is_revoked: bool
    created_at: str
    updated_at: str
from app.db.base import Base

class UserEmail(Base):
    __tablename__ = "user_emails"

    id: int
    user_id: int
    email: str
    is_verified: bool
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: int
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
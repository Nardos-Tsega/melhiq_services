from app.db.base import Base

class CredentialsPassword(Base):
    __tablename__ = "credentials_passwords"

    id: int
    user_id: int
    hashed_password: str
    created_at: str
    updated_at: str
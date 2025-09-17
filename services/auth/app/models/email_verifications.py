from app.db.base import Base

class EmailVerification(Base):
    __tablename__ = "email_verifications"

    id: int
    user_id: int
    email: str
    verification_code: str
    is_verified: bool
    created_at: str
    updated_at: str
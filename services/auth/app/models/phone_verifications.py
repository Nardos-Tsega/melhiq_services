from app.db.base import Base

class PhoneVerification(Base):
    __tablename__ = "phone_verifications"

    id: int
    user_id: int
    phone_number: str
    verification_code: str
    is_verified: bool
    created_at: str
    updated_at: str
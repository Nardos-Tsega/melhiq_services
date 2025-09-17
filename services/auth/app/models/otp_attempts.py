from app.db.base import Base

class OtpAttempt(Base):
    __tablename__ = "otp_attempts"

    id: int
    user_id: int
    otp_code: str
    is_used: bool
    created_at: str
    updated_at: str
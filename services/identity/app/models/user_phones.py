from app.db.base import Base

class UserPhone(Base):
    __tablename__ = "user_phones"

    id: int
    user_id: int
    phone_number: str
    is_verified: bool
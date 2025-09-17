from app.db.base import Base

class Membership(Base):
    __tablename__ = "memberships"

    id: int
    user_id: int
    role_id: int
    tenant_id: int
    is_active: bool
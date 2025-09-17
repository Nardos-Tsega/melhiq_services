from app.db.base import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id: int
    name: str
    is_active: bool
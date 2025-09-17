from app.db.base import Base

class Permission(Base):
    __tablename__ = "permissions"

    id: int
    name: str
    description: str
    is_active: bool
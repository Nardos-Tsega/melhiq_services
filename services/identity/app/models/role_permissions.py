from app.db.base import Base

class RolePermission(Base):
    __tablename__ = "role_permissions"

    id: int
    role_id: int
    permission: str
    is_granted: bool
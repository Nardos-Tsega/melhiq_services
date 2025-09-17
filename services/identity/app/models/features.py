from app.db.base import Base

class Feature(Base):
    __tablename__ = "features"

    id: int
    name: str
    description: str
    is_active: bool
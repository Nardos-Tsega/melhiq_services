from app.db.base import Base

class Agent(Base):
    __tablename__ = "agents"

    id: int
    name: str
    email: str
    is_active: bool
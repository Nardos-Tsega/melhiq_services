from app.db.base import Base

class Broker(Base):
    __tablename__ = "brokers"

    id: int
    name: str
    api_key: str
    is_active: bool
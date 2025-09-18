from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, Integer, DateTime, func

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    
    phone: Mapped[str] = mapped_column(
        String(15),
        nullable=True,
        unique=True
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True    
    )
    
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
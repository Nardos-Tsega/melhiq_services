from app.db.base import Base

class TenantFeature(Base):
    __tablename__ = "tenant_features"

    id: int
    tenant_id: int
    feature_name: str
    is_enabled: bool
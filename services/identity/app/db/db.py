from app.config.settings import get_settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

settings = get_settings()

engine = create_async_engine(
    settings.database_url,
    echo=settings.echo_sql,
    pool_pre_ping=True
)

SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
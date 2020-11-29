from uuid import uuid4

from melldechof.dbtypes import DbPresence, UUID
from sqlalchemy import Column, ForeignKey, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True, nullable=False, default=uuid4)
    email = Column(String(128), unique=True)
    name = Column(String(128))

    presences = relationship("Presence", back_populates="user")


class Presence(Base):
    __tablename__ = "presence"
    user_id = Column(
        UUID,
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
    )
    event_id = Column(String(128), primary_key=True)
    presence = Column(DbPresence)

    user = relationship("User", back_populates="presences")

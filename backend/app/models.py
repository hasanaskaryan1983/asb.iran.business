from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Horse(Base):
    __tablename__ = "horses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    breed = Column(String(100))
    age = Column(Integer)
    gender = Column(String(20))
    color = Column(String(50))
    height = Column(Integer)
    province = Column(String(100))
    city = Column(String(100))
    price = Column(Integer)
    negotiable = Column(Boolean, default=False)
    discipline = Column(String(100))
    has_pedigree = Column(Boolean, default=False)
    has_rank = Column(Boolean, default=False)
    description = Column(Text)
    seller_name = Column(String(255))
    seller_phone = Column(String(20))
    photo_url = Column(String(500))
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String(20), default="active")

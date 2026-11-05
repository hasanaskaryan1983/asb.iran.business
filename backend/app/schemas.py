from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class HorseBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    breed: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=50)
    gender: Optional[str] = None
    color: Optional[str] = None
    height: Optional[int] = Field(None, ge=50, le=250)
    province: Optional[str] = None
    city: Optional[str] = None
    price: Optional[int] = Field(None, ge=0)
    negotiable: bool = False
    discipline: Optional[str] = None
    has_pedigree: bool = False
    has_rank: bool = False
    description: Optional[str] = None
    seller_name: Optional[str] = None
    seller_phone: Optional[str] = None
    photo_url: Optional[str] = None
    is_premium: bool = False

class HorseCreate(HorseBase):
    pass

class HorseUpdate(HorseBase):
    pass

class HorseResponse(HorseBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    status: str

    class Config:
        orm_mode = True

class HorseListResponse(BaseModel):
    total: int
    horses: List[HorseResponse]

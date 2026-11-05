from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas, database

app = FastAPI(
    title="اسب ایران API",
    description="API برای بازار آنلاین خرید و فروش اسب در ایران",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def root():
    return {"message": "به API اسب ایران خوش آمدید! 🐎"}

@app.get("/api/horses", response_model=List[schemas.HorseResponse])
def get_horses(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    breed: Optional[str] = None,
    province: Optional[str] = None,
    db: Session = Depends(database.get_db)
):
    query = db.query(models.Horse).filter(models.Horse.status == "active")
    if breed:
        query = query.filter(models.Horse.breed == breed)
    if province:
        query = query.filter(models.Horse.province == province)
    return query.offset(skip).limit(limit).all()

@app.get("/api/horses/{horse_id}", response_model=schemas.HorseResponse)
def get_horse(horse_id: int, db: Session = Depends(database.get_db)):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="اسب مورد نظر یافت نشد")
    return horse

@app.post("/api/horses", response_model=schemas.HorseResponse)
def create_horse(horse: schemas.HorseCreate, db: Session = Depends(database.get_db)):
    db_horse = models.Horse(**horse.dict())
    db.add(db_horse)
    db.commit()
    db.refresh(db_horse)
    return db_horse

@app.put("/api/horses/{horse_id}", response_model=schemas.HorseResponse)
def update_horse(
    horse_id: int,
    horse_update: schemas.HorseUpdate,
    db: Session = Depends(database.get_db)
):
    db_horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not db_horse:
        raise HTTPException(status_code=404, detail="اسب مورد نظر یافت نشد")
    for key, value in horse_update.dict(exclude_unset=True).items():
        setattr(db_horse, key, value)
    db.commit()
    db.refresh(db_horse)
    return db_horse

@app.delete("/api/horses/{horse_id}")
def delete_horse(horse_id: int, db: Session = Depends(database.get_db)):
    db_horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not db_horse:
        raise HTTPException(status_code=404, detail="اسب مورد نظر یافت نشد")
    db_horse.status = "removed"
    db.commit()
    return {"message": "آگهی با موفقیت حذف شد"}

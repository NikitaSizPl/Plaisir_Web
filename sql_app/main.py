from fastapi import FastAPI, Depends
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import product_model, crud

app = FastAPI()

product_model.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/category/")
async def get_all_category(db: Session = Depends(get_db)):
    category = crud.get_all_category(db)
    return category


@app.get("/category/{cat_id}/items/")
async def read_one_by_category(cat_id: int, db: Session = Depends(get_db)):
    only_one_category = crud.get_one_by_category(cat_id, db)
    return only_one_category


@app.get("/category/{cat_id}/items/{item_id}")
async def read_product_by_id(cat_name: str, item_id: int, db: Session = Depends(get_db)):
    only_one_item_id = crud.get_product_by_id(cat_name, item_id, db)
    return only_one_item_id

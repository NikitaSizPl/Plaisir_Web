from fastapi import FastAPI, Depends
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sql_app import product_model, crud

app = FastAPI()

product_model.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=['10 items'])
async def ten_itims(db: Session = Depends(get_db)):
    return None


@app.get("/category/", tags=['all_category'])
async def get_all_category(db: Session = Depends(get_db)):
    category = crud.get_all_category(db)
    return category


@app.get("/category/{cat_id}/items/", tags=['all_in_one_category'])
async def read_one_by_category(cat_id: int, db: Session = Depends(get_db)):
    only_one_category = crud.get_one_by_category(cat_id, db)
    return only_one_category


@app.get("/category/{cat_id}/items/{item_id}", tags=['one_in_one_category'])
async def read_product_by_id(cat_id: int, item_id: int, db: Session = Depends(get_db)):
    only_one_item_id = crud.get_product_by_id(cat_id, item_id, db)
    return only_one_item_id

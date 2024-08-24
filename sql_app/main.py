from fastapi import FastAPI, Depends, HTTPException, Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sql_app import product_model, crud
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Настраиваем шаблоны
templates = Jinja2Templates(directory="templates")

product_model.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=['Home'], response_class=HTMLResponse)
async def ten_itims(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Home"})


@app.get("/category", tags=['all_category'], response_class=HTMLResponse)
async def get_all_category(request: Request, db: Session = Depends(get_db)):
    category = crud.get_all_category(db)
    if category is None:
        raise HTTPException(status_code=400, detail="Category not found ERROR")
    return templates.TemplateResponse(
        "all_categor.html", {"request": request, "name": "category", "category": category})


@app.get("/category/{cat_id}/items", tags=['all_in_one_category'], response_class=HTMLResponse)
async def read_one_by_category(request: Request, cat_id: int, db: Session = Depends(get_db)):
    only_one_category = crud.get_one_by_category(cat_id, db)
    if only_one_category is None:
        raise HTTPException(status_code=400, detail="Category not found ERROR")
    return templates.TemplateResponse(
        "one_categor.html", {"request": request, "name": "only_one_category", "only_one_category": only_one_category})


@app.get("/category/{cat_id}/items/{item_id}", tags=['one_in_one_category'], response_class=HTMLResponse)
async def read_product_by_id(request: Request, cat_id: int, item_id: int, db: Session = Depends(get_db)):
    only_one_item_id = crud.get_product_by_id(cat_id, item_id, db)
    if only_one_item_id is None:
        raise HTTPException(status_code=400, detail="Item not found in Category ERROR")
    return templates.TemplateResponse(
        "item.html", {"request": request, "name": "item", "only_one_item_id": only_one_item_id})


@app.get("/contact", tags=['contact'], response_class=HTMLResponse)
async def get_contact(request: Request):
    return templates.TemplateResponse(
        "contact.html", {"request": request, "name": "contact"})


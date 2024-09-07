from fastapi import Depends, HTTPException, Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates
from app import crud
from app.database import SessionLocal, engine
from app.models import product_model

router = APIRouter()

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


@router.get("/category", tags=['product'], response_class=HTMLResponse)
async def get_all_category(request: Request, db: Session = Depends(get_db)):
    category = crud.get_all_category(db)
    if category is None:
        raise HTTPException(status_code=400, detail="Category not found ERROR")
    return templates.TemplateResponse(
        "all_categor.html", {"request": request, "name": "category", "category": category})

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from .product import templates, get_db
from .. import crud

router = APIRouter(
    prefix="/category",
    tags=["product"],
)


@router.get("/{cat_id}/items", tags=['product'], response_class=HTMLResponse)
async def read_one_by_category(request: Request, cat_id: int, db: Session = Depends(get_db)):
    only_one_category = crud.get_one_by_category(cat_id, db)
    if only_one_category is None:
        raise HTTPException(status_code=400, detail="Category not found ERROR")
    return templates.TemplateResponse(
        "one_categor.html", {"request": request, "name": "only_one_category", "only_one_category": only_one_category})


@router.get("/{cat_id}/items/{item_id}", tags=['product'], response_class=HTMLResponse)
async def read_product_by_id(request: Request, cat_id: int, item_id: int, db: Session = Depends(get_db)):
    only_one_item_id = crud.get_product_by_id(cat_id, item_id, db)
    if only_one_item_id is None:
        raise HTTPException(status_code=400, detail="Item not found in Category ERROR")
    return templates.TemplateResponse(
        "item.html", {"request": request, "name": "item", "only_one_item_id": only_one_item_id}
    )

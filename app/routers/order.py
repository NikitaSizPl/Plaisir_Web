from typing import List
from fastapi import APIRouter, Request
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from app.models.order_model import Order
from app.routers.product import templates

router = APIRouter(
    prefix="/order",
    tags=['order']
)

# Временное  хранилище заказов
orders = []


@router.post("/", tags=['order'], response_model=Order, response_class=HTMLResponse)
async def create_order(order: Order, request: Request):
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")
    orders.append(order)
    return templates.TemplateResponse(
        "orders.html", {"request": request, "name": "order", "order": order})


@router.get("/", tags=['order'], response_model=List[Order], response_class=HTMLResponse)
async def get_orders(request: Request):
    if not orders:  # Проверка на наличие заказов
        raise HTTPException(status_code=404, detail="No orders found")
    return templates.TemplateResponse(
        "order.html", {"request": request, "name": "orders", "orders": orders})

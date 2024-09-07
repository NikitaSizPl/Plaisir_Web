from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from .routers.product import templates
from .routers import product_items, product, order
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(product.router)
app.include_router(product_items.router)
app.include_router(order.router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Home"})


@app.get("/contact", response_class=HTMLResponse)
async def get_contact(request: Request):
    return templates.TemplateResponse(
        "contact.html", {"request": request, "name": "contact"})

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.db import async_session_factory
from database.models import Product
from sqlalchemy import select
from fastapi import HTTPException
router = APIRouter()
templates = Jinja2Templates(directory="templates")



@router.get("/products", response_class=HTMLResponse)
async def list_products(request: Request):
    async with async_session_factory() as session:
        result = await session.execute(select(Product))
        products = result.scalars().all()
        return templates.TemplateResponse("products.html", {
        "request":request,
        "products": products
    })


@router.get("/products/{product_id}", response_class=HTMLResponse)
async def product_detail(request: Request, product_id: int):
    async with async_session_factory() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product = result.scalar_one_or_none()

        if product is None:
            raise HTTPException(status_code=404, detail="Товар не найден")

        return templates.TemplateResponse("product.html", {
            "request": request,
            "product": product
        })

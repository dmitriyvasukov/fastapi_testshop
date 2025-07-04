from fastapi import APIRouter, Request, UploadFile, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database.models import Product
from database.db import async_session_factory
import shutil
import os


router = APIRouter()

templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static/img"

@router.get("/admin/add-product")
async def add_product_form(request: Request):
    return templates.TemplateResponse("add_product.html", {"request":request})


@router.post("/admin/add-product")
async def add_product(
    request: Request,
    name: str = Form(...),
    price: int = Form(...),
    image: UploadFile = Form(...)
):
    image_path = os.path.join(UPLOAD_DIR, image.filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    async with async_session_factory() as session:
        new_product = Product(name=name, price=price, image=f"img/{image.filename}")
        session.add(new_product)
        await session.commit()

    return RedirectResponse(url="/products", status_code=303)        
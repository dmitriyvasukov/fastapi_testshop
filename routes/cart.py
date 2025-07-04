from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status

router = APIRouter()

templates = Jinja2Templates(directory="templates")


CART = {}

@router.get("/cart")
async def view_cart(request: Request):
    return templates.TemplateResponse("cart.html", {
        "request" : request,
        "cart" : CART
    })


@router.post("/cart/add")
async def add_to_cart(
    request: Request,
    product_id: int = Form(...),
    product_name: str = Form(...),
    product_price: int = Form(...)
):
    if product_id in CART:
        CART[product_id]["quantity"] += 1
    else:
        CART[product_id] = {
            "name":product_name,
            "price": product_price,
            "quantity": 1
        }

    return RedirectResponse("/cart", status_code=status.HTTP_303_SEE_OTHER)



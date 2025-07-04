from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette import status
from routes import products, cart, admin


class App(FastAPI): 
    def __init__(self):
        super().__init__()
        self.mount("/static", StaticFiles(directory="static"), name="static")
        self.templates = Jinja2Templates(directory="templates")

        self.include_routes()

        self.router.add_api_route("/", self.redirect_to_products)

    async def redirect_to_products(self, request: Request):
        return RedirectResponse("/products", status_code=status.HTTP_302_FOUND)
    
    def include_routes(self):
        self.include_router(products.router)
        self.include_router(cart.router)
        self.include_router(admin.router)



import asyncio
from database.db import async_session_factory
from database.models import Product

async def seed():
    async with async_session_factory() as session:
        session.add_all(
            [
                Product(name="ESP32", price=300, image="img/esp32.jpg"),
                Product(name="HCSR04", price=150, image="img/hcsr04.jpg"),
                Product(name="ESP32", price=300, image="img/mg996.jpg")

            ]
        )
        await session.commit()

asyncio.run(seed())
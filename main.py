from fastapi import FastAPI
from controllers import payment_controller

app = FastAPI(title="Meemoo Payment API")

app.include_router(payment_controller.router)

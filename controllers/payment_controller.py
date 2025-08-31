from fastapi import APIRouter
from services.payment_service import PaymentService
from models.payment_models import (
    PaymentRequestCreate,
    PaymentRequest,
)

router = APIRouter()

@router.get("/payment_request/{id}", response_model=PaymentRequest)
async def get_payment_request(id: str):
    return PaymentService.read_payment_request(id)

@router.post("/payment_requests", response_model=PaymentRequest)
async def create_payment_request(req: PaymentRequestCreate):
    return PaymentService.create_payment_request(req)

@router.post("/payment_attempts")
async def create_payment_attempt():
    return {"Coming soon in your neighbourhood!"}

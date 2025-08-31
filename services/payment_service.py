from datetime import datetime, timedelta
from fastapi import HTTPException
from repositories.payment_request_repository import PaymentRequestRepository
from repositories.payment_attempt_repository import PaymentAttemptRepository

class PaymentService:
    @staticmethod
    def create_payment_request(data):
        now = datetime.now()
        valid_till = now + timedelta(hours=data.valid_duration_in_hours)
        return PaymentRequestRepository.create(
            data.requester_id, data.amount_in_cents, data.currency, valid_till, now
        )

    @staticmethod
    def read_payment_request(id):
        return PaymentRequestRepository.find_by_id(id)

    @staticmethod
    def create_payment_attempt(data):
        now = datetime.now()
        request = PaymentRequestRepository.find_by_id(data.requester_id)
        if not request:
            raise HTTPException(status_code=404, detail="Payment request not found")

        if request["status"] != "PENDING":
            raise HTTPException(status_code=400, detail="Payment request is not pending")

        if datetime.fromisoformat(request["valid_till"]) < datetime.now():
            PaymentRequestRepository.update_status(request["id"], "EXPIRED")
            raise HTTPException(status_code=400, detail="Payment request has expired")

        attempt = PaymentAttemptRepository.create(
            data.payer_id, data.requester_id, data.amount_in_cents, data.currency, now
        )

        PaymentRequestRepository.update_status(request["id"], "COMPLETED")
        return attempt

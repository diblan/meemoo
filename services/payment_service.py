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

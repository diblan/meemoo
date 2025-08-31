from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints
from datetime import datetime

class PaymentRequest(BaseModel):
    id: int
    requester_id: int
    amount_in_cents: int
    currency: str
    valid_till: datetime
    status: str
    created_at: datetime

class PaymentRequestCreate(BaseModel):
    requester_id: int
    amount_in_cents: Annotated[int, Field(gt=0)]
    currency: Annotated[str, StringConstraints(to_upper=True, pattern=r'^(EUR|USD)$')]
    valid_duration_in_hours: Annotated[int, Field(gt=0)]

class PaymentAttemptCreate(BaseModel):
    payer_id: int
    requester_id: int
    amount_in_cents: Annotated[int, Field(gt=0)]
    currency: Annotated[str, StringConstraints(to_upper=True, pattern=r'^(EUR|USD)$')]

class PaymentAttempt(BaseModel):
    id: int
    payer_id: int
    requester_id: int
    amount_in_cents: int
    currency: str
    status: str
    created_at: datetime

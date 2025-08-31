import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path

DB_PATH = Path("database.sqlite")

app = FastAPI()

class PaymentRequest(BaseModel):
    id: int
    requester_id: int
    amount_in_cents: int
    currency: str
    valid_till: datetime
    status: str
    created_at: datetime


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/payment_request/{id}", response_model=PaymentRequest)
async def get_payment_request(id: str):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM payment_request WHERE id = ?", (id,))
    row = cursor.fetchone()
    connection.close()
    return dict(row) if row else None

@app.post("/payment_requests")
async def payment_requests():
    return {"Coming soon in your neighbourhood!"}
    
@app.post("/payment_attempts")
async def payment_attempts():
    return {"Coming soon in your neighbourhood!"}

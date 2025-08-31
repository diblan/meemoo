from db import get_db

class PaymentAttemptRepository:
    @staticmethod
    def create(payer_id, requester_id, amount_in_cents, currency, created_at):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO payment_attempt (payer_id, requester_id, amount_in_cents, currency, status, created_at)
            VALUES (?, ?, ?, ?, 'COMPLETED', ?)
            """,
            (payer_id, requester_id, amount_in_cents, currency, created_at),
        )
        connection.commit()
        new_id = cursor.lastrowid
        cursor.execute("SELECT * FROM payment_attempt WHERE id = ?", (new_id,))
        row = dict(cursor.fetchone())
        connection.close()
        return row

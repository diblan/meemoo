from db import get_db

class PaymentRequestRepository:
    @staticmethod
    def create(requester_id, amount_in_cents, currency, valid_till, created_at):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO payment_request (requester_id, amount_in_cents, currency, valid_till, status, created_at)
            VALUES (?, ?, ?, ?, 'PENDING', ?)
            """,
            (requester_id, amount_in_cents, currency, valid_till, created_at),
        )
        connection.commit()
        new_id = cursor.lastrowid
        cursor.execute("SELECT * FROM payment_request WHERE id = ?", (new_id,))
        row = dict(cursor.fetchone())
        connection.close()
        return row

    @staticmethod
    def find_by_id(request_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM payment_request WHERE id = ?", (request_id,))
        row = cursor.fetchone()
        connection.close()
        return dict(row) if row else None

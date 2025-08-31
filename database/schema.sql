CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE CHECK (length(username) <= 255),
    email TEXT NOT NULL UNIQUE CHECK (length(email) <= 255),
    password_hash TEXT NOT NULL CHECK (length(password_hash) = 60),
    first_name TEXT NOT NULL CHECK (length(first_name) <= 255),
    last_name TEXT NOT NULL CHECK (length(last_name) <= 255),
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS payment_request (
    id INTEGER PRIMARY KEY,
    requester_id INTEGER NOT NULL,
    amount_in_cents INTEGER NOT NULL,
    currency TEXT NOT NULL CHECK (currency IN ('EUR', 'USD')) DEFAULT ('EUR'),
    valid_till TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('PENDING', 'COMPLETED', 'CANCELLED', 'EXPIRED')) DEFAULT ('PENDING'),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (requester_id) REFERENCES users (id),
    CHECK (valid_till >= created_at)
);

CREATE TABLE IF NOT EXISTS payment_attempt (
    id INTEGER PRIMARY KEY,
    payer_id INTEGER,
    requester_id INTEGER NOT NULL,
    amount_in_cents INTEGER NOT NULL,
    currency TEXT NOT NULL CHECK (currency IN ('EUR', 'USD')) DEFAULT ('EUR'),
    status TEXT NOT NULL CHECK (status IN ('COMPLETED', 'CANCELLED')),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (payer_id) REFERENCES users (id),
    FOREIGN KEY (requester_id) REFERENCES users (id)
);

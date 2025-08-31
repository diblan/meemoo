-- Seed users (Flemish names)
INSERT INTO users (username, email, password_hash, first_name, last_name)
VALUES
    ('pietpiraat', 'piet.piraat@example.com',
     'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
     'Piet', 'Piraat'),
    ('renemagritte', 'rene.magritte@example.com',
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
     'René', 'Magritte'),
    ('pieterdeconinck', 'pieter.de.coninck@example.com',
     'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc',
     'Pieter', 'de Coninck'),
    ('janbreydel', 'jan.breydel@example.com',
     'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd',
     'Jan', 'Breydel'),
    ('joskevermeulen', 'joske.vermeulen@example.com',
     'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
     'Joske', 'Vermeulen');

-- Seed payment requests
INSERT INTO payment_request (requester_id, amount_in_cents, currency, valid_till, status)
VALUES
    (1, 30, 'EUR', datetime('now', '+7 days'), 'COMPLETED'),     -- Piet requests €30
    (2, 45, 'USD', datetime('now', '+10 days'), 'PENDING'),    -- René requests $45
    (3, 125, 'EUR', datetime('now', '+5 days'), 'COMPLETED'),  -- Pieter requests €125
    (4, 20, 'EUR', datetime('now', '+14 days'), 'COMPLETED'),    -- Jan requests €20
    (5, 80, 'USD', datetime('now', '+21 days'), 'CANCELLED');  -- Joske requests $80

-- Seed payment attempts
INSERT INTO payment_attempt (payer_id, requester_id, amount_in_cents, currency, status)
VALUES
    (2, 1, 30, 'EUR', 'COMPLETED'),    -- René pays Piet
    (3, 2, 45, 'USD', 'CANCELLED'),    -- Pieter attempted to pay René
    (4, 3, 125, 'EUR', 'COMPLETED'),   -- Jan pays Pieter
    (5, 4, 20, 'EUR', 'COMPLETED'),    -- Joske pays Jan
    (1, 5, 80, 'USD', 'CANCELLED');    -- Piet attempted to pay Joske

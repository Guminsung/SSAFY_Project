CREATE Table transactions(
    id PRIMARY key,
    user_id INTEGER,
    amount TEXT,
    transaction_date DATE,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO transactions (user_id, amount, transaction_date) VALUES(1, 500, '2024-03-15');
INSERT INTO transactions (user_id, amount, transaction_date) VALUES(2, 700, '2024-03-16');
INSERT INTO transactions (user_id, amount, transaction_date) VALUES(3, 200, '2024-03-17');
INSERT INTO transactions (user_id, amount, transaction_date) VALUES(4, 1000, '2024-03-18');

SELECT 
    u.first_name,
    u.last_name,
    t.amount, 
    t.transaction_date
FROM
    transactions t
JOIN
    users u ON t.user_id = u.id;

UPDATE users 
SET last_name = '홍' 
WHERE first_name = '길동';
SELECT 
    u.first_name,
    u.last_name,
    t.amount, 
    t.transaction_date
FROM
    users u
JOIN
    transactions t ON u.id = t.user_id
WHERE
    t.transaction_date > '2024-03-16';

SELECT 
    u.first_name,
    u.last_name,
    sum(amount) total_amount
FROM
    users u
JOIN
    transactions t ON u.id = t.user_id
GROUP BY
    u.first_name;




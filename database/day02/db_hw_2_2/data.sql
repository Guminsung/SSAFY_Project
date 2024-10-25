CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    total_amount REAL
);

CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
);

INSERT INTO orders (order_id, order_date, total_amount) VALUES(1, '2023-07-15', 50.99);
INSERT INTO orders (order_id, order_date, total_amount) VALUES(2, '2023-07-16', 75.5);
INSERT INTO orders (order_id, order_date, total_amount) VALUES(3, '2023-07-17', 30.25);

INSERT INTO customers (customer_id, name, email, phone) VALUES(1, '허균', 'hong.gildong@example.com', '010-1234-5678');
INSERT INTO customers (customer_id, name, email, phone) VALUES(2, '김영희', 'kim.younghee@example.com', '010-9648-5432');
INSERT INTO customers (customer_id, name, email, phone) VALUES(3, '이철수', 'lee.cheolsu@example.com', '010-5555-4444');

DELETE  
FROM orders
WHERE order_id = 3;

UPDATE customers
SET name = '홍길동'
WHERE customer_id = 1;

SELECT * FROM customers;
SELECT * FROM orders;
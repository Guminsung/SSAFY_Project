SELECT *
FROM users
WHERE age > 30 AND balance > 1000;

SELECT *
FROM users
WHERE balance <= 1000 AND age <= 20;

SELECT *
FROM users
WHERE first_name LIKE '현%' 
    AND country LIKE '제주%' 
    AND age = (
        SELECT MAX(age) 
        FROM users 
        WHERE first_name LIKE '현%' 
            AND country LIKE '제주%'
);

SELECT * 
FROM users
WHERE last_name = '박' 
    AND age >= 25
    AND age = (
        SELECT MIN(age) 
        FROM users
        WHERE last_name = '박'
        AND age >= 25
);

SELECT *
FROM users
WHERE first_name = '재은' or first_name = '영일' 
    AND balance = (
        SELECT max(balance)
        FROM users
        WHERE first_name = '재은' or first_name = '영일'
    );

SELECT first_name, last_name, age, phone, country, max(balance) as max_balance
FROM users
GROUP BY country
ORDER BY balance DESC;

SELECT *
FROM users
WHERE age >= 30 
    AND balance >  (
        SELECT avg(balance) as avg_balance
        FROM users
        WHERE age >= 30
    );
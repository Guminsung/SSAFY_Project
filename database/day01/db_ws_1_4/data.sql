SELECT * FROM users;

SELECT avg(age) as average_age 
FROM users

SELECT country, count(*) as user_count 
FROM users
GROUP BY country;

SELECT * 
FROM users
WHERE balance = (SELECT MAX(balance) FROM users);

SELECT country, avg(balance) as avg_balance
FROM users
GROUP BY country;

SELECT max(balance) - min(balance) as balance_difference
FROM users;
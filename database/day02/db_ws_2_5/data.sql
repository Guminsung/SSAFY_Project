SELECT *
FROM employees;

SELECT * 
FROM departments;

SELECT 
    d.name AS department_name,
    e.name AS employee_name,
    MAX(e.age) AS max_age,
    AVG(e.age) AS avg_age
FROM 
    departments d
JOIN
    employees e ON d.id = e.departmentId
GROUP BY
    d.name
HAVING 
    e.age = (SELECT MAX(age) 
              FROM employees 
              WHERE departmentId = d.id);

SELECT 
    d.name AS department_name,
    e.name AS highest_paid_employee,
    MAX(e.salary) AS max_salary
FROM 
    departments d
JOIN
    employees e ON d.id = e.departmentId
GROUP BY
    d.name
HAVING 
    e.salary = (SELECT MAX(salary) 
              FROM employees 
              WHERE departmentId = d.id);

SELECT 
    d.name AS department_name,
    CASE 
        WHEN e.age < 30 THEN 'under 30'
        WHEN e.age BETWEEN 30 AND 40 THEN 'between 30 and 40'
        ELSE 'over 40'
    END AS age_group,
    COUNT(*) AS employee_count
FROM 
    departments d
JOIN
    employees e ON d.id = e.departmentId
GROUP BY
    d.name,
    CASE 
        WHEN e.age < 30 THEN 'under 30'
        WHEN e.age BETWEEN 30 AND 40 THEN 'between 30 and 40'
        ELSE 'over 40'
    END
ORDER BY
    d.name, age_group;

SELECT 
    d.name AS department,
    AVG(e.salary) AS avg_salary_excluding_highest
FROM 
    departments d
JOIN 
    employees e ON d.id = e.departmentId
WHERE 
    e.salary < (
        SELECT MAX(salary)
        FROM employees e2
        WHERE e2.departmentId = d.id
    )
GROUP BY 
    d.id, d.name
ORDER BY 
    avg_salary_excluding_highest DESC;

INSERT INTO employees(id, name, salary, age, "departmentId") VALUES(10, '이규보', 150000, 77, 1);
INSERT INTO employees(id, name, salary, age, "departmentId") VALUES(11, '김구', 126000, 55, 2);
INSERT INTO employees(id, name, salary, age, "departmentId") VALUES(12, '유관순', 82000, 19, 4);
INSERT INTO employees(id, name, salary, age, "departmentId") VALUES(13, '김병년', 100000000, 27, 3);


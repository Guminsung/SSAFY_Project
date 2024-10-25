SELECT *
FROM hotels;

UPDATE hotels 
SET grade = UPPER(grade);

SELECT grade
FROM hotels;

CREATE Table customers(
    id PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE reservations(
    id PRIMARY KEY,
    customer_id TEXT,
    room_num TEXT,
    check_in TEXT,
    check_out TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(room_num) REFERENCES hotels(room_num)
);

PRAGMA table_info(reservations);
PRAGMA foreign_key_list(reservations);

INSERT INTO customers(id, name, email) VALUES('1', '홍길동', 'john@example.com');
INSERT INTO customers(id, name, email) VALUES('2', '박지영', 'jane@example.com');
INSERT INTO customers(id, name, email) VALUES('3', '김미영', 'alice@example.com');
INSERT INTO customers(id, name, email) VALUES('4', '이철수', 'bob@example.com');

INSERT INTO reservations(id, customer_id, room_num, check_in, check_out) VALUES('1', '1', '101', '2024-03-20', '2024-03-25');
INSERT INTO reservations(id, customer_id, room_num, check_in, check_out) VALUES('2', '2', '202', '2024-03-21', '2024-03-24');
INSERT INTO reservations(id, customer_id, room_num, check_in, check_out) VALUES('3', '3', '303', '2024-03-22', '2024-03-26');
INSERT INTO reservations(id, customer_id, room_num, check_in, check_out) VALUES('4', '4', '404', '2024-03-23', '2024-03-27');

SELECT * FROM reservations;
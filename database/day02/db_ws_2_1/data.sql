
CREATE Table zoo(
    Name TEXT,
    eat TEXT,
    weight INT,
    height INT,
    age INT
);

INSERT INTO zoo("Name", eat, weight, height, age) VALUES('코끼리', '채소', 5000, 300, 5);
INSERT INTO zoo("Name", eat, weight, height, age) VALUES('사자', '고기', 200, 120, 15);
INSERT INTO zoo("Name", eat, weight, height, age) VALUES('원숭이', '채소', 50, 60, 10);
INSERT INTO zoo("Name", eat, weight, height, age) VALUES('기린', '채소', 1500, 550, 8);
INSERT INTO zoo("Name", eat, weight, height, age) VALUES('개', '채소', 30, 100, 6);

SELECT * FROM zoo;
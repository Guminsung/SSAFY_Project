ALTER TABLE zoo 
ADD COLUMN species Text;


UPDATE zoo
SET species = 'Panthera leo'
WHERE name = 'Lion';

UPDATE zoo
SET species = 'Giraffa camelopardails'
WHERE name = 'Giraffe';

UPDATE zoo
SET species = 'Loxodonta africana'
WHERE name = 'Elephant';

UPDATE zoo
SET species = 'Cebus capucinus'
WHERE name = 'Monkey';

UPDATE zoo
SET height = height * 2.54;

SELECT * FROM zoo;
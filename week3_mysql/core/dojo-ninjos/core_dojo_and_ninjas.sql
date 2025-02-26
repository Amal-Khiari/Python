-- Forward engineer the dojos_and_ninjas_schema from the previous chapter
-- (Assuming the schema has already been forward-engineered)

-- Query: Create 3 new dojos
INSERT INTO dojos (name) VALUES ('Dojo Alpha');
INSERT INTO dojos (name) VALUES ('Dojo Beta');
INSERT INTO dojos (name) VALUES ('Dojo Gamma');

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id IN (1, 2, 3);

-- Query: Create 3 more dojos
INSERT INTO dojos (name) VALUES ('Dojo Delta');
INSERT INTO dojos (name) VALUES ('Dojo Epsilon');
INSERT INTO dojos (name) VALUES ('Dojo Zeta');

-- Query: Create 3 ninjas that belong to the first dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Naruto', 'Uzumaki', 17, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Sasuke', 'Uchiha', 17, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Sakura', 'Haruno', 17, 4);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Kakashi', 'Hatake', 30, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Shikamaru', 'Nara', 18, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Hinata', 'Hyuga', 17, 5);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Gaara', 'Sabaku', 19, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Rock', 'Lee', 18, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Neji', 'Hyuga', 18, 6);

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo
SELECT dojos.* FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = (SELECT MAX(id) FROM ninjas);

-- Query: Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo

SELECT ninjas.*, dojos.name AS dojo_name FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 6;

-- Query: Use a JOIN to retrieve all the ninjas as well as that ninja's dojo

SELECT ninjas.*, dojos.name AS dojo_name FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id;
##Select All Names:

SELECT * FROM names;
#Insert a Name:
INSERT INTO names (name, created_at, updated_at) VALUES ('AMAL KHIARI', NOW(), NOW());

SELECT * FROM names;

#Insert Multiple Names:

INSERT INTO names (name, created_at, updated_at) VALUES 
('MAHER CHAABENI', NOW(), NOW()),
('YASMINE CHARFEDI', NOW(), NOW());

#Delete a Name:
DELETE FROM names WHERE id = 1;

#Update a Name:
UPDATE names SET name = 'ITEB KHIARI' WHERE id = 1;
#Create 3 New Users:
iNSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('John', 'Doe', 'john.doe@example.com', NOW(), NOW()),
       ('Jane', 'Smith', 'jane.smith@example.com', NOW(), NOW()),
       ('Alice', 'Johnson', 'alice.johnson@example.com', NOW(), NOW());
       
 #Retrieve All Users:
 SELECT * FROM users;
 
 #Retrieve the First User by Email:
 SELECT * FROM users WHERE email = 'john.doe@example.com';
 
 #Retrieve the Last User by ID:
SELECT * FROM users WHERE id = (SELECT MAX(id) FROM users);

#Change User's Last Name:
UPDATE users SET last_name = 'Pancakes' WHERE id = 3;

#Delete User:
DELETE FROM users WHERE id = 2;

#Sort Users by First Name:
SELECT * FROM users ORDER BY first_name ASC;

#Bonus: Sort Users by First Name in Descending Order:
SELECT * FROM users ORDER BY first_name DESC;
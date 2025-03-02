# drop them if they already exist to avoid conflicts !!!!!

DROP TABLE IF EXISTS friendships;
DROP TABLE IF EXISTS users;

#Create the  Tables

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    created_at DATETIME,
    updated_at DATETIME
);
CREATE TABLE friendships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    friend_id INT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

# verify the schema by describing the tables !!!!!!!!!!!!!!!!!!!!
DESCRIBE users; 
DESCRIBE friendships;

#Create 6 New Users 

INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES
('Amy', 'Giver', NOW(), NOW()),
('Eli', 'Byers', NOW(), NOW()),
('Big', 'Bird', NOW(), NOW()),
('Kermit', 'The Frog', NOW(), NOW()),
('Marky', 'Mark', NOW(), NOW()),
('John', 'Doe', NOW(), NOW());

#Establish Friendships
INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES
(1, 2, NOW(), NOW()),
(1, 4, NOW(), NOW()),
(1, 6, NOW(), NOW()),
(2, 1, NOW(), NOW()),
(2, 3, NOW(), NOW()),
(2, 5, NOW(), NOW()),
(3, 2, NOW(), NOW()),
(3, 5, NOW(), NOW()),
(4, 3, NOW(), NOW()),
(5, 1, NOW(), NOW()),
(5, 6, NOW(), NOW()),
(6, 2, NOW(), NOW()),
(6, 3, NOW(), NOW());


#Display Relationships
SELECT u1.first_name, u1.last_name, u2.first_name AS friend_first_name, u2.last_name AS friend_last_name
FROM users u1
JOIN friendships f ON u1.id = f.user_id
JOIN users u2 ON f.friend_id = u2.id;

#NINJA Queries
#!!Friends of the First User

SELECT u2.first_name, u2.last_name
FROM friendships f
JOIN users u2 ON f.friend_id = u2.id
WHERE f.user_id = 1;

#!!Count of All Friendships

SELECT COUNT(*) AS total_friendships FROM friendships;

#!!User with the Most Friends

SELECT user_id, COUNT(*) AS friend_count
FROM friendships
GROUP BY user_id
ORDER BY friend_count DESC
LIMIT 1;

#!!Friends of the Third User in Alphabetical Order

SELECT u2.first_name, u2.last_name
FROM friendships f
JOIN users u2 ON f.friend_id = u2.id
WHERE f.user_id = 3
ORDER BY u2.first_name, u2.last_name;

SELECT * FROM users;
SELECT * FROM friendships;
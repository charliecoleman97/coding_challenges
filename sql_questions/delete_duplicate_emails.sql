-- DELETE DUPLICATE EMAILS

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Person table:
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Output: 
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+
-- Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

-- TABLE PREP

CREATE TABLE Person (
    id int, 
    email VARCHAR(255)
);

INSERT INTO Person VALUES
(1, 'john@example.com'),
(2, 'bob@example.com'),
(3, 'john@example.com');
-- (4, 'gav@example.com'),
-- (5, 'bob@example.com'),
-- (6, 'john@example.com');



-- QUESTION ATTEMPT

DELETE 
FROM Person
WHERE id NOT IN
(SELECT min(id) As id
FROM Person
GROUP BY email);

SELECT *
FROM Person;

-- Pretty sure this works but the leetcode terminal said every attempt was wrong (even the solution) 
-- so just going to assume this is fine


-- Answer I found that works nicely 
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id


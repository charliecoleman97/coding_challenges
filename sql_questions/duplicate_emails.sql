-- DUPLICATE EMAILS QUESTION

-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Person table:
-- +----+---------+
-- | id | email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- Output: 
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Explanation: a@b.com is repeated two times.

-- Table Prep
CREATE TABLE Person(
    id int, 
    email varchar(100)
);


INSERT INTO Person VALUES
(1, 'a@b.com'),
(2, 'c@d.com'),
(3, 'a@b.com')

SELECT * 
FROM Person;

-- Answer to Question
SELECT DISTINCT(email)
FROM Person
WHERE email IN
(SELECT email FROM Person GROUP BY email HAVING COUNT(*) > 1);
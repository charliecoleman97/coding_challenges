-- CUSTOMERS WHO NEVER ORDER QUESTION

-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example 1:

-- Input: 
-- Customers table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+
-- Orders table:
-- +----+------------+
-- | id | customerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+
-- Output: 
-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+

-- TABLE PREP
CREATE TABLE Customers(
    id int,
    name VARCHAR(100)
)

CREATE TABLE Orders(
    id int, 
    customerID int
)

INSERT INTO Customers VALUES
(1, 'Joe'),
(2, 'Henry'),
(3, 'Sam'),
(4, 'Max'),
(5, 'Joe');

INSERT INTO Orders VALUES
(1, 3),
(2, 1)

-- QUESTION ATTEMPT
SELECT name as Customers
FROM Customers
WHERE id NOT IN
(
SELECT t1.id
FROM Customers t1, Orders t2
WHERE t1.id = t2.customerID
);


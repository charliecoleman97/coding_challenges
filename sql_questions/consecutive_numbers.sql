-- CONSECTUTIVE NUMBERS

-- Write an SQL query to find all numbers that appear at least three times consecutively.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.

-- TABLE PREP

CREATE TABLE Logs(
    id INT, 
    num INT
)

INSERT INTO logs VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 1),
(6, 2),
(7, 2)

-- QUESTION ATTEMPT
SELECT DISTINCT(t1.num)
FROM logs t1, logs t2, logs t3
WHERE t1.id = t2.id -1 and t2.id = t3.id-1
and t1.num = t2.num and t2.num = t3.num;



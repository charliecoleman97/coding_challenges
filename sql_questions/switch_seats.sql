-- SWAP SEATS

-- Write an SQL query to swap the seat id of every two consecutive students. 
-- If the number of students is odd, the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.
-- The query result format is in the following example.

-- Input: 
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output: 
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+
-- Explanation: 
-- Note that if the number of students is odd, there is no need to change the last one's seat.

-- TABLE PREP

CREATE TABLE Seat (
    id INT,
    student VARCHAR(255)
)

INSERT INTO Seat VALUES
(1, 'Abbot'),
(2, 'Doris'),
(3, 'Emerson'),
(4, 'Green'),
(5, 'Jeames')

SELECT *
FROM Seat
WHERE id %2 = 0;

-- QUESTION ATTEMPT
SELECT 
    CASE 
        WHEN (SELECT COUNT(*) FROM Seat)%2 = 0 THEN
            CASE
                WHEN id %2 = 0 THEN id -1 
                ELSE id + 1
            END 
        ELSE 
            CASE 
                WHEN (SELECT COUNT(*) FROM Seat) = id THEN id
                WHEN id % 2 = 0 THEN id -1 
                ELSE id + 1
            END
    END AS id,
student
FROM Seat
ORDER BY id ASC;


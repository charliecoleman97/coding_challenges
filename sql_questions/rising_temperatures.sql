-- RISING TEMPERATURES

-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
-- The query result format is in the following example.

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

-- TABLE PREP

CREATE TABLE Weather(
    id int,
    recordDate DATE,
    temperature int
);

INSERT INTO Weather VALUES
(1, '2015-01-01', 10),
(2, '2015-01-02', 25),
(3, '2015-01-03', 20),
(4, '2015-01-04', 30);


-- QUESTION ATTEMPT
SELECT * 
FROM Weather;


SELECT wt1.id
FROM Weather wt1, Weather wt2
WHERE DATEDIFF(DAY, wt1.recordDate,wt2.recordDate) = -1 AND wt1.temperature > wt2.temperature;

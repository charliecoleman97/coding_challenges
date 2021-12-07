-- Write an SQL query to report the second highest salary from the Employee table. 
-- If there is no second highest salary, the query should report null.
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- TABLE PREP

CREATE TABLE Employee(
    id int, 
    salary int
);
GO

INSERT INTO Employee VALUES
(1, 100),
(2, 200), 
(3,300)
GO

-- ANSWER

SELECT MAX(salary)
FROM Employee
WHERE salary not in 
(SELECT MAX(salary) from Employee)


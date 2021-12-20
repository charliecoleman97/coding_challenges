-- NTH HIGHEST SALARY
-- Write an SQL query to report the nth highest salary from the Employee table. 
-- If there is no nth highest salary, the query should report null.

-- The query result format is in the following example.
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- n = 2
-- Output: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

-- Example 2:
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- n = 2
-- Output: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | null                   |
-- +------------------------+

-- TABLE PREP
-- CREATE TABLE Employee (
--     id INT, 
--     salary BIGINT
-- )

-- INSERT INTO Employee VALUES
-- (1, 100),
-- (2, 200),
-- (3, 300);

-- Need to comment out the table prep as function needs to come first

-- SELECT salary
-- FROM Employee
-- ORDER BY salary DESC
-- OFFSET 0 ROWS
-- FETCH NEXT 1 ROW ONLY;

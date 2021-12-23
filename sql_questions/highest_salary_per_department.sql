-- DEPARTMENT HIGHEST SALARY

-- Write an SQL query to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example 1:

-- Input: 
-- Employee table:
-- +----+-------+--------+--------------+
-- | id | name  | salary | departmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- Department table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | IT    |
-- | 2  | Sales |
-- +----+-------+
-- Output: 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- | IT         | Max      | 90000  |
-- +------------+----------+--------+
-- Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.


-- TABLE PREP

CREATE TABLE Employee (
    id INT, 
    name VARCHAR(255),
    salary BIGINT,
    departmentId INT
)

INSERT INTO Employee VALUES
(1, 'Joe', 70000, 1),
(2, 'Jim', 90000, 1),
(3, 'Henry', 80000, 2),
(4, 'Sam', 60000, 2),
(5, 'Max', 90000, 1)

CREATE TABLE Department (
    id INT,
    name VARCHAR(255)
)

INSERT INTO Department VALUES
(1, 'IT'),
(2, 'Sales')

-- QUESTION ATTEMPT

WITH CTE_Employee AS (
    SELECT departmentId,id,
    MAX(salary) OVER (PARTITION BY departmentId) as Max_Salary
    FROM Employee)

SELECT t2.name as Department, t1.name as Employee, t1.salary as Salary
FROM Employee t1, Department t2, CTE_Employee t3
WHERE t1.salary = t3.Max_Salary AND t1.id = t3.id AND t1.departmentId = t2.id;

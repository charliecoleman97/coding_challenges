-- Reformat Department Table

-- Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example 1:
-- Input: 
-- Department table:
-- +------+---------+-------+
-- | id   | revenue | month |
-- +------+---------+-------+
-- | 1    | 8000    | Jan   |
-- | 2    | 9000    | Jan   |
-- | 3    | 10000   | Feb   |
-- | 1    | 7000    | Feb   |
-- | 1    | 6000    | Mar   |
-- +------+---------+-------+
-- Output: 
-- +------+-------------+-------------+-------------+-----+-------------+
-- | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
-- +------+-------------+-------------+-------------+-----+-------------+
-- | 1    | 8000        | 7000        | 6000        | ... | null        |
-- | 2    | 9000        | null        | null        | ... | null        |
-- | 3    | null        | 10000       | null        | ... | null        |
-- +------+-------------+-------------+-------------+-----+-------------+
-- Explanation: The revenue from Apr to Dec is null.
-- Note that the result table has 13 columns (1 for the department id + 12 for the months).

-- Table Prep
CREATE TABLE Department (
    id INT, 
    revenue BIGINT,
    month VARCHAR(255)
)

INSERT INTO Department VALUES
(1, 8000, 'Jan'),
(2, 9000, 'Jan'),
(3, 10000, 'Feb'),
(1, 7000, 'Feb'),
(1, 6000, 'Mar');

-- QUESTION ATTEMPT
SELECT id, month
FROM Department
GROUP BY month, id

select id, 
sum(case month when 'Jan' then revenue else Null end) as Jan_Revenue, 
sum(case month when 'Feb' then revenue else Null end) as Feb_Revenue,
sum(case month when 'Mar' then revenue else Null end) as Mar_Revenue,
sum(case month when 'Apr' then revenue else Null end) as Apr_Revenue,
sum(case month when 'May' then revenue else Null end) as May_Revenue,
sum(case month when 'Jun' then revenue else Null end) as Jun_Revenue,
sum(case month when 'Jul' then revenue else Null end) as Jul_Revenue,
sum(case month when 'Aug' then revenue else Null end) as Aug_Revenue,
sum(case month when 'Sep' then revenue else Null end) as Sep_Revenue,
sum(case month when 'Oct' then revenue else Null end) as Oct_Revenue,
sum(case month when 'Nov' then revenue else Null end) as Nov_Revenue,
sum(case month when 'Dec' then revenue else Null end) as Dec_Revenue
from Department
group by id

SELECT id, 
SUM(IIF(month = 'Jan', revenue, Null)) as Jan_Revenue,
SUM(IIF(month = 'Feb', revenue, Null)) as Feb_Revenue,
SUM(IIF(month = 'Mar', revenue, Null)) as Mar_Revenue,
SUM(IIF(month = 'Apr', revenue, Null)) as Apr_Revenue,
SUM(IIF(month = 'May', revenue, Null)) as May_Revenue,
SUM(IIF(month = 'Jun', revenue, Null)) as Jun_Revenue,
SUM(IIF(month = 'Jul', revenue, Null)) as Jul_Revenue,
SUM(IIF(month = 'Aug', revenue, Null)) as Aug_Revenue,
SUM(IIF(month = 'Sep', revenue, Null)) as Sep_Revenue,
SUM(IIF(month = 'Oct', revenue, Null)) as Oct_Revenue,
SUM(IIF(month = 'Nov', revenue, Null)) as Nov_Revenue,
SUM(IIF(month = 'Dec', revenue, Null)) as Dec_Revenue
FROM Department
GROUP BY id;

-- Both work and checked if case is faster than iif but looks like it's similar speed just case can be used in 
-- all SQL languages whereas IIF is exlcusive MSSQL 2012+ 
-- Basically IIF is the same as when CASE WHEN <Condition> THEN <true part> ELSE <false part> END.


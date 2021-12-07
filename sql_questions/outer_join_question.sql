-- QUESTION 

-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

-- Return the result table in any order.




-- TABLE PREP 
CREATE TABLE Person(
    personId int,
    lastName varchar(100),
    firstName varchar(100)
); 
GO

CREATE TABLE Address(
    addressId int, 
    personID int, 
    city VARCHAR(100), 
    state varchar(100)
);
GO


INSERT INTO Person VALUES
(1, 'Wang', 'Allen'), 
(2, 'Alice', 'Bob')

INSERT INTO Address VALUES
(1, 2, 'New York City', 'New York'), 
(2, 3, 'San Diego', 'California')


-- ANSWER TO QUESTION
SELECT a.firstName, a.lastName, b.city, b.state 
FROM Person a 
LEFT OUTER JOIN Address b 
ON a.personId = b.personID;



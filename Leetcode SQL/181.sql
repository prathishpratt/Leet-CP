# Write your MySQL query statement below
SELECT A.name AS Employee
FROM Employee A
INNER JOIN Employee B
ON A.managerID = B.id 
WHERE A.salary > B.salary

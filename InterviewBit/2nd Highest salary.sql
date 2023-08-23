SELECT distinct a.salary
FROM employees as a
INNER JOIN departments as b
ON a.department_id = b.id 
WHERE b.name = 'engineering'
-- GROUP BY salary
ORDER BY salary DESC
LIMIT 1,1 
-- it skips the 
-- first 1 value and then return the next 1 entry
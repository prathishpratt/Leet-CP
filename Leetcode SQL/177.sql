CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      SELECT (
          SELECT DISTINCT Salary
          FROM Employee 
          ORDER BY Salary DESC
          LIMIT 1 OFFSET M) 
            AS getNthHighestSalary
      
  );
END
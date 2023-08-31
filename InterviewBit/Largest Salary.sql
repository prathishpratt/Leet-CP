SELECT department, max(salary) as largest_salary
FROM employees
GROUP BY department
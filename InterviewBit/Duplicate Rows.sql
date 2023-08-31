-- SELECT id,name,created_at
-- FROM users
-- GROUP BY 1,2,3
-- HAVING COUNT(*)>1

WITH rows_ AS(
    SELECT users.*,
    ROW_NUMBER() OVER(PARTITION BY id, name, created_at) AS rowk_
    FROM users   
)

SELECT rows_.id, rows_.name, rows_.created_at
FROM rows_
WHERE rowk_ >1
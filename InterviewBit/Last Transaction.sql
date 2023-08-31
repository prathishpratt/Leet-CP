WITH E AS (
    SELECT x.*,
    RANK() OVER(PARTITION BY DATE(created_at) ORDER BY created_at DESC) AS date_rank
    FROM bank_transactions as x
)

SELECT E.id, E.created_at, E.transaction_value
FROM E
WHERE date_rank = 1

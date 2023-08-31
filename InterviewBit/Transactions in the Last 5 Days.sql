SELECT Count(*) as number_of_users
FROM (select user_id  from bank_transactions
WHERE DATE(created_at) BETWEEN '2020-01-01' AND '2020-01-05'
Group by user_id
Having count(DISTINCT DATE(created_at)) =5) as sub

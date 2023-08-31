SELECT query, ROUND(avg(RAT),2) AS avg_rating
FROM (SELECT query, (rating/position) AS RAT
FROM search_results) AS s
GROUP BY query
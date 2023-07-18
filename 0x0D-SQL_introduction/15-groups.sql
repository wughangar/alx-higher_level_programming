-- script that lists number of records with same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY SCORE
ORDER BY number DESC;

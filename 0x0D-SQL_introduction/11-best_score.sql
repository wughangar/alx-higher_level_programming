-- script that lists all records from second table scores in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

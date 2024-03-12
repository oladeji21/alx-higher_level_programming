-- SCript that lists all records with a score >= 10 from the second_table of our database
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

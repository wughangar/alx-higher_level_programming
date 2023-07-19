-- script that lists all the cities of california that can be found in the database
SELECT cities FROM state
WHERE cities = 'California'
ORDER BY cities.id ASC;

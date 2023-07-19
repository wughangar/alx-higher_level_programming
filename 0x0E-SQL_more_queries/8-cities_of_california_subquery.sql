-- script that lists all the cities of california that can be found in the database
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id IN (SELECT states.id FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;

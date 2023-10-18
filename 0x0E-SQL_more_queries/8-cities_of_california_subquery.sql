-- Lists all the cities of California found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states 
WHERE cities.state_id = (SELECT id from states WHERE name = 'California')
AND states.name = 'California'
ORDER BY cities.id ASC;

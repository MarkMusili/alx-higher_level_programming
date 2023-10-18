-- Lists all the cities of California found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities 
WHERE cities.state_id = (SELECT id from states WHERE name = 'California') 
ORDER BY cities.id ASC;

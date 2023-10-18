-- Lists all the cities of California found in the database hbtn_0d_usa
SELECT id, name FROM cities 
WHERE cities.state_id = (SELECT id from states WHERE name = 'California') 
ORDER BY id ASC;

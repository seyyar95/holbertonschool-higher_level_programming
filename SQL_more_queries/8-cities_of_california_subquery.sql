--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE id=(SELECT * FROM states WHERE name = 'california') ORDER BY (id);

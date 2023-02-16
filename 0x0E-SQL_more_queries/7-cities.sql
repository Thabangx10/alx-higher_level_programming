-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- Description(cities): id(INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY)
--                      state_id(INT NOT NULL FORIGN KEY->FROM states table(id))
--                      name(VARCHAR(256) NOT NULL)
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities
(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id)
);

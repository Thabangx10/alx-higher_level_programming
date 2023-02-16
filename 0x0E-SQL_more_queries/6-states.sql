-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- Description(States table): id(INT UNIQUE AUTO INCREMENT NOT NULL PRIMARY KEY) 
--                            name(VARCHAR(256) NOT NULL)
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Connect to your database, 'USE', to create your table(states)
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states
(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) not null,
PRIMARY KEY(id)
);

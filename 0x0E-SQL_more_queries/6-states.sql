-- scripts that creates data base and table inside data base 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select database to create table in
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

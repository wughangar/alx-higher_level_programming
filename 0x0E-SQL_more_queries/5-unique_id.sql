-- script that creates unique_id with default, primary key constraints
CREATE TABLE IS NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

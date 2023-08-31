-- script that creates second_table
CREATE TABLE IF NOT EXISTS second_table(
	id int,
	name VARCHAR(216),
	score int
);

-- this cript inserts values into the table respectively
INSERT INTO second_table(id, name, score) VALUES(1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES(4, 'George', 8);

-- connect to mysql server
mysql -u root -p

-- script that lists the privilages of particular users in localhost
SHOW GRANTS FOR 'user_0d_1'@localhost;

-- script to list grants for user user_0d_2
SHOW GRANTS FOR 'user_0d_2'@localhost;

-- exit mysql
EXIT

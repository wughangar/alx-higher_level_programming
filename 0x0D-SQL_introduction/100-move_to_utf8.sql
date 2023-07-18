-- converting database into UTF8
-- first modify data base encoding
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- switch to database before converting table
USE hbtn_0c_0;

-- Modify table encoding
ALTER TABLE first_table DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

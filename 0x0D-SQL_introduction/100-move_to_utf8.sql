-- converting database into UTF8
-- first modify data base encoding
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Modify table encoding
USE hbtn_0c_0;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- modify the columb encoding
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

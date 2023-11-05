/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that creates all the base tables to be used in the project
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call initialize_baseTables ();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS initialize_baseTables$$

CREATE PROCEDURE initialize_baseTables ()
BEGIN
   
    
	CREATE TABLE IF NOT EXISTS `userDetails`(
		userName VARCHAR(30) NOT NULL PRIMARY KEY, 
        userPassword VARCHAR(25) NOT NULL,
        user_firstName NVARCHAR(128),
        user_lastName NVARCHAR(128),
        user_emailID NVARCHAR(320) UNIQUE        
		);
        
	-- drop fk constraints and tables
    ALTER TABLE itemDetails  DROP CONSTRAINT  `itemdetails_ibfk_1`; 
	ALTER TABLE userReviews DROP CONSTRAINT  `userreviews_ibfk_1`; 
    ALTER TABLE userReviews DROP CONSTRAINT `userreviews_ibfk_2`; 
    DROP TABLE `itemDetails`;
	DROP TABLE `userReviews`;
	
	
	Call p_insert_to_initialize_baseTables();
	      
END$$
DELIMITER ; 

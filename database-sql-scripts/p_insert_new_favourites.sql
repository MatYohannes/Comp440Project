/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure to get insert common Favorites.
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-20 10:48:12
    
    execution statement example: 
                   CALL p_insert_new_favourites('adminUser', 'mya', @output_message);
                       select @output_message;
			
*/ 


DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_insert_new_favourites$$

-- Procedure to insert a new item into the database
CREATE PROCEDURE p_insert_new_favourites(
  IN current_userName varchar(30),  
  IN favourites_userName varchar(30),
  OUT result_message  VARCHAR(255)
)
BEGIN
	 
	CREATE TABLE IF NOT EXISTS `userFavourites`(
		favouriteID INT AUTO_INCREMENT PRIMARY KEY, 
        userName VARCHAR(30) NOT NULL,
        favourite_userName varchar(30)      
		);
		
	 INSERT INTO `comp440_database_project`.`userFavourites`(`userName`,
														`favourite_userName`)
		 VALUES (current_userName,favourites_userName);
         
	 set result_message =  concat('Favourite User Inserted for: ', current_userName);
     
     select result_message;
	
END  $$

DELIMITER ;
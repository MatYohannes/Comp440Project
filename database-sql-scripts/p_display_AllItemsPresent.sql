/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that displays all the item Details present in the db
					without any filtering
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call p_display_AllItemsPresent ();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_display_AllItemsPresent$$

CREATE PROCEDURE p_display_AllItemsPresent ()
BEGIN
	SELECT itemTitle 'Item Title', itemDescription 'Item Description', itemCategory 'Item Category' , itemPrice 'Price' , DateofListing as 'Listed On'
	  FROM  itemDetails;
    
END$$
DELIMITER ;
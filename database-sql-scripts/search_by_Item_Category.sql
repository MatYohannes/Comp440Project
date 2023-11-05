/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will  return all items in the category to be used in our project
    Created By: Devamsh K
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call search_by_Item_Category('category');

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS search_by_Item_Category$$
  
-- Procedure to search items by category
CREATE PROCEDURE search_by_Item_Category(
  IN search_category VARCHAR(255) 
)
BEGIN 
     
  -- Select items that match the provided category
  SELECT itemCategory, itemTitle, itemDescription, itemPrice 
    FROM itemDetails
   WHERE itemCategory LIKE concat('%', search_category,'%');
   
END$$

DELIMITER ;
/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will  return all items in the category to be used in our project
    Created By: Devamsh K
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call search_by_Item_Category('category', @output_message); 

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS search_by_Item_Category$$
  
-- Procedure to search items by category
CREATE PROCEDURE search_by_Item_Category(
  IN search_category VARCHAR(255) ,
  OUT output_message varchar(255)
)
BEGIN 
     
  -- Select items that match the provided category
    DECLARE result_count INT;

    -- Check if there are items in the specified category
    SELECT COUNT(*) INTO result_count
    FROM itemDetails
    WHERE itemCategory LIKE CONCAT('%', search_category, '%');

    -- If there are items, return them; otherwise, return 'no values found'
    IF result_count > 0 THEN
          SELECT itemCategory, itemTitle, itemDescription, itemPrice 
			FROM itemDetails
		   WHERE itemCategory LIKE concat('%', search_category,'%');
    ELSE
		SET output_message = 'no values found in the category';
        SELECT output_message;
    END IF;
    
END$$

DELIMITER ;
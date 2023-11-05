/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will insert new items into the item table
					to be used in our project
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call p_insert_new_item( current_userName,   itemTitle,  itemDescription ,   itemCategory,   itemPrice  ,  item_listingDate);

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_insert_new_item$$

-- Procedure to insert a new item into the database
CREATE PROCEDURE p_insert_new_item(
  IN current_userName varchar(30),  
  IN itemTitle VARCHAR(255),  
  IN itemDescription TEXT,  
  IN itemCategory VARCHAR(255),  
  IN itemPrice DECIMAL(10, 2) ,
  IN item_listingDate DATE
)
BEGIN
  DECLARE today_items INT;

  -- Count the number of items posted by the user today
  SELECT COUNT(*)
  INTO today_items
  FROM itemDetails 
  WHERE userName = current_userName
    AND DateofListing = item_listingDate;

  -- Check if the user has already posted 3 items today
  IF today_items > 3 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'You can only post 3 items a day';
    
  ELSE
    -- Insert the new item into the database
    INSERT INTO itemDetails 
		 VALUES (itemTitle, itemDescription , itemCategory, itemPrice, current_userName, item_listingDate);
  END IF;
END $$

DELIMITER ;
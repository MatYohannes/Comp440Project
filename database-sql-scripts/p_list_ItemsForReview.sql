/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will list all the items for review that arent created by the current user
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call p_list_ItemsForReview(userName);

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_list_ItemsForReview$$

-- Procedure to list items for a review  
CREATE PROCEDURE p_list_ItemsForReview(IN ReviewerUserName varchar(30)
)
BEGIN
       SELECT itemTitle, itemDescription, itemCategory, itemPrice
		FROM itemDetails 
	   WHERE userName !=  ReviewerUserName;
       
END$$

DELIMITER ;
/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will list all the items by a user which are excellent or good. 
    Created By: Twishi Saran , Devamsh kondragunta
    Updated On:  2023-11-19 21:28:26
    
    execution statement example: 
			CALL Find_Items_With_Positive_Comments('adminUser');


*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Find_Items_With_Positive_Comments$$

-- create a procedure that will list all the items by a user which are excellent or good. 

CREATE PROCEDURE Find_Items_With_Positive_Comments(
    IN currentUserName VARCHAR(30)
)
BEGIN
		  SELECT i.*
			FROM itemDetails i
			JOIN userReviews ur ON i.itemID = ur.itemID
			WHERE ur.userName = currentUserName
				AND ur.userReview IN ('Excellent', 'Good')
				AND NOT EXISTS (
					SELECT 1
					FROM userReviews
					WHERE itemID = i.itemID
						AND userReview IN ('Poor', 'Fair')
						);
END $$

DELIMITER ;

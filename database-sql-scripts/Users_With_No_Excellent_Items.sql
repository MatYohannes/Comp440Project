/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script to create a procedure that selects users who have never posted any "excellent" items. 
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-20 10:29:45
    
    execution statement example: 
               CALL Users_With_No_Excellent_Items();
                   
			
*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Users_With_No_Excellent_Items$$

-- Procedure to select users who have never posted any "excellent" items. 
CREATE PROCEDURE Users_With_No_Excellent_Items()
BEGIN
    -- Find users who never posted any "excellent" items
    SELECT DISTINCT i.userName
			FROM itemDetails i
			LEFT JOIN userReviews r
				   ON i.itemID = r.itemID
			WHERE r.userReview IS NULL
				OR NOT EXISTS (
					SELECT 1
					FROM userReviews
					WHERE userReview = 'Excellent'
					HAVING COUNT(*) >= 3
				);
END $$

DELIMITER ;
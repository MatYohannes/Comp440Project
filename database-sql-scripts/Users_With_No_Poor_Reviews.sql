/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script to create a procedure that finds users with no poor reviews.
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-20 11:39:33
    
    execution statement example: 
               CALL Users_With_No_Poor_Reviews();
                   
*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Users_With_No_Poor_Reviews$$

-- Procedure to find users with no poor reviews

CREATE PROCEDURE Users_With_No_Poor_Reviews()
BEGIN
    -- Find all users who never posted a "poor" review
     SELECT DISTINCT d.userName
			    FROM userDetails d
		   LEFT JOIN userReviews r 
				  ON d.userName = r.userName 
                  AND r.userReview = 'Poor'
				WHERE r.userName IS NULL;

END $$

DELIMITER ;

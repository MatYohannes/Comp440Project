/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This script will create a procedure that displays users with poor reviews
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-21 15:10:54
    
    execution statement example: 
			Call Users_With_Only_Poor_Reviews();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Users_With_Only_Poor_Reviews$$

-- Procedure to display users with poor reviews

CREATE PROCEDURE Users_With_Only_Poor_Reviews()
BEGIN
    -- Find users who posted some reviews, but each of them is "poor"
    SELECT DISTINCT u.userName
    FROM userDetails u
    JOIN userReviews r ON u.userName = r.userName
    WHERE u.userName NOT IN (
        SELECT DISTINCT r1.userName
        FROM userReviews r1
        WHERE r1.userReview <> 'Poor'
    );
END $$

DELIMITER ;

/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure to find user pairs who always gave each other "excellent" reviews
    Created By: Twishi Saran , Devamsh Kondragunta
    Updated On:  2023-11-22 18:44:33
    
    execution statement example: 
			call Find_User_Pairs_With_Excellent_Reviews();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Find_User_Pairs_With_Excellent_Reviews$$

-- Procedure to find user pairs who always gave each other "excellent" reviews

CREATE PROCEDURE Find_User_Pairs_With_Excellent_Reviews()
BEGIN
    SELECT DISTINCT r1.reviewer AS UserA, r2.reviewer AS UserB
    FROM reviews r1
    JOIN reviews r2 ON r1.itemID = r2.itemID AND r1.reviewer != r2.reviewer
    WHERE r1.reviewType = 'Excellent' AND r2.reviewType = 'Excellent'
        AND NOT EXISTS (
            SELECT 1
            FROM reviews r3
            WHERE r3.itemID = r1.itemID
                AND r3.reviewer IN (r1.reviewer, r2.reviewer)
                AND r3.reviewType != 'Excellent'
        );
END $$

DELIMITER ;
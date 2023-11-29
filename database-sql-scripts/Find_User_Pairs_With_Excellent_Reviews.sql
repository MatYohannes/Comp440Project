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
		DROP TEMPORARY TABLE IF EXISTS user_pairs;
        
		CREATE TEMPORARY TABLE user_pairs AS
				SELECT DISTINCT
					i.userName AS UserA,
					r.userName AS UserB
				FROM itemDetails i
				JOIN  userReviews r ON i.ItemID = r.ItemID
				WHERE NOT EXISTS (
						SELECT 1
						FROM   userReviews r2
						WHERE   r2.ItemID = i.ItemID 
							AND r2.userReview <> 'Excellent'
					)
					AND NOT EXISTS (
						SELECT 1
						FROM userReviews r3
						WHERE r3.ItemID = i.ItemID 
							AND r3.userReview <> 'Excellent'
					);

		SELECT DISTINCT
			LEAST(UserA, UserB) AS User1,
			GREATEST(UserA, UserB) AS User2
		from user_pairs;
        
        
        
END $$

DELIMITER ;
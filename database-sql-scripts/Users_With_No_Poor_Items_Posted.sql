/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure to find users whose posted items have never received any "poor" reviews or have not received any reviews at all
    Created By: Twishi Saran , Devamsh Kondragunta
    Updated On:  2023-11-21 17:48:16
    
    execution statement example: 
			call Users_With_No_Poor_Items_Posted();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Users_With_No_Poor_Items_Posted$$

-- Procedure to Find users whose posted items have never received any "poor" reviews or have not received any reviews at all
DELIMITER $$

CREATE PROCEDURE Users_With_No_Poor_Items_Posted()
BEGIN
		               
                  SELECT i.userName,  count(distinct poorItems.itemID) poorItemsPosted
					FROM itemDetails i
					LEFT JOIN ( SELECT DISTINCT itemID
											FROM userReviews
											WHERE userReview = 'Poor'
								) AS poorItems 
							ON i.itemID = poorItems.itemID
					GROUP BY i.userName
                    HAVING  count(distinct poorItems.itemID) = 0;

END $$

DELIMITER ;

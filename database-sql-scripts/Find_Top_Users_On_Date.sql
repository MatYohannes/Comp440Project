/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This script will create a procedure to List the users who posted the most number of items on a specific date;
    Created By: Twishi Saran , Devamsh kondragunta
    Updated On:  2023-11-20 8:47:52
    
    execution statement example: 
			CALL Find_Top_Users_On_Date('2023-11-05');
*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Find_Top_Users_On_Date$$

-- create a procedure to List the users who posted the most number of items on a specific date;

CREATE PROCEDURE Find_Top_Users_On_Date(
    IN targetDate DATE
)
BEGIN
		WITH UserItemCounts AS (
		SELECT  userName,
				DateofListing,
				COUNT(itemID) AS itemCount,
				dense_rank() OVER (PARTITION BY DateofListing ORDER BY COUNT(itemID) DESC) AS rnk
		FROM itemDetails
		GROUP BY userName, DateofListing
		)
		SELECT userName, DateofListing
		FROM UserItemCounts
		WHERE rnk = 1 
          and DateofListing = targetDate;
END $$

DELIMITER ;

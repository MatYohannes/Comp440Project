/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will list users who posted at least two items that were posted on the same day.
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-19 21:10:34
    
    execution statement example: 
                       CALL Find_Users_With_Two_Items_Same_Day('electronics', 'office');

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Find_Users_With_Two_Items_Same_Day$$

-- create a procedure that will list users who posted at least two posted at least two items that were posted on the same day.
CREATE PROCEDURE Find_Users_With_Two_Items_Same_Day(
    IN categoryX VARCHAR(255),
    IN categoryY VARCHAR(255)
)
BEGIN
   

			SELECT   X.userName as Category1UserName,  
					 categoryX as itemCategory, 
                     count(distinct X.itemTitle) as ItemsPostedbyUserInCategory1, 
                     MAX(X.DateofListing) as DateofListing,
                     
                     Y.userName as Category2UserName, 
					 categoryY as itemCategory, 
                     count(distinct Y.itemTitle) as ItemsPostedbyUserInCategory2, 
                     MAX(Y.DateofListing) as DateofListing
			FROM itemDetails AS X
			JOIN itemDetails AS Y ON X.userName = Y.userName
								  AND X.DateofListing = Y.DateofListing
								  AND X.itemID <> Y.itemID
			WHERE X.itemCategory LIKE CONCAT('%', categoryX, '%') 
				AND Y.itemCategory  LIKE CONCAT('%', categoryY, '%') 
		   GROUP BY X.userName,  Y.userName
		   HAVING COUNT(DISTINCT X.itemID) >= 2 ;

END $$

DELIMITER ;

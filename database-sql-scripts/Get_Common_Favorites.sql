/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure to get common Favorites.
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-20 10:48:12
    
    execution statement example: 
                   CALL Get_Common_Favorites('userX', 'userY');
			
*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS Get_Common_Favorites$$

-- Procedure to get common Favorites

CREATE PROCEDURE Get_Common_Favorites(
    IN userX VARCHAR(30),
    IN userY VARCHAR(30)
)
BEGIN
  
	SELECT DISTINCT uf1.favourite_userName  AS CommonFavorite 
				FROM userFavourites uf1
				JOIN userFavourites uf2 
					ON uf1.favourite_userName = uf2.favourite_userName
				WHERE uf1.userName  = userX
                  AND uf2.userName = userY;

END $$

DELIMITER ;

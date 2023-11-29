/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure to get common Favorites.
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-20 10:48:12
    
    execution statement example: 
                   CALL GetCommonFavorites('userX', 'userY');
			
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
    -- Create a temporary table to store the favorites of X and Y
    CREATE TEMPORARY TABLE temp_favorites AS
    SELECT userName
    FROM favorites
    WHERE favoritedBy = userX;

    -- Insert favorites of Y into the temporary table
    INSERT INTO temp_favorites
    SELECT userName
    FROM favorites
    WHERE favoritedBy = userY;

    -- Retrieve the users who are common favorites for X and Y
    SELECT userName
    FROM temp_favorites
    GROUP BY userName
    HAVING COUNT(userName) = 2;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_favorites;
END $$

DELIMITER ;

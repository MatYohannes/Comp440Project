/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will list out the expensive items in each category  
    Created By: Twishi Saran, Devamsh Kondragunta
    Updated On:  2023-11-19 20:55:06
    
    execution statement example: 
                  CALL List_Most_Expensive_Items();
                  
*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS List_Most_Expensive_Items$$

-- Procedure to list expensive items in each category
CREATE PROCEDURE List_Most_Expensive_Items()
BEGIN
    -- Select the most expensive items for each category using a subquery
    WITH RankedItems AS (
    SELECT
        itemID,
        itemTitle,
        itemDescription,
        itemCategory,
        itemPrice,
        DENSE_RANK() OVER (PARTITION BY itemCategory ORDER BY itemPrice DESC) AS RankOrder
    FROM
        itemDetails
	)
	SELECT
		itemID,
		itemTitle,
		itemDescription,
		itemCategory,
		itemPrice
	FROM
		RankedItems
	WHERE
		RankOrder = 1;
END $$

DELIMITER ;

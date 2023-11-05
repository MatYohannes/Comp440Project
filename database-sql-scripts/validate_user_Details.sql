/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that is called in UI to
					get validate the user details in the database of our project
    Created By: Twishi Saran
    Updated On: 2023-10-07 17:22:22
    
    execution statement example: 
			CALL check_userDetails("userName","userPassword","userEmail",  @ValidationResult);
			SELECT @ValidationResult; 

*/

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS check_userDetails$$

CREATE PROCEDURE check_userDetails (IN user_Name VARCHAR(30), 
									IN user_Password VARCHAR(25),
									IN user_EmailID NVARCHAR(320),
                                    OUT ValidationResult VARCHAR(255)) 
BEGIN
	  
    DECLARE var_userName varchar(30); 
    DECLARE var_userPswd  varchar(25); 
    DECLARE var_userEmail varchar(320);
    DECLARE userCount varchar(10);
	 
	SET var_userName = user_Name;
    SET var_userPswd = user_Password;
    SET var_userEmail = user_EmailID; 
   

    -- Check if any of the input parameters are null
    IF var_userName IS NULL OR var_userEmail IS NULL OR var_userPswd IS NULL THEN
        SET ValidationResult = 'Invalid Input';
        
    ELSE
        -- Check if the combination exists in the database
        SELECT IF(COUNT(distinct userName)  > 0, 'true', 'false') INTO userCount
         FROM comp440_database_project.userDetails
        WHERE (userName = var_userName OR user_emailID = var_userEmail)
          AND userPassword = var_userPswd;
          
            -- Set the result based on the userCount
        IF userCount = 'true' THEN
            SET ValidationResult = 'User Exists';
        ELSE
            SET ValidationResult = 'User Does Not Exist';
        END IF;
          
    END IF;
    
    SELECT ValidationResult;
    
END$$
DELIMITER ;
 



 
/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details:  This stored procedure is used for login 
    Created By: Twishi Saran
    Updated On: 2023-10-07 17:22:22
    
    execution statement example: 
			CALL  p_login_user(userName, userPswd, @ValidationResult);
			SELECT @ValidationResult; 

*/

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_login_user$$

create procedure p_login_user(		IN user_Name VARCHAR(30), 
									IN user_Password VARCHAR(25),
                                    OUT ValidationResult VARCHAR(255))
BEGIN	
    -- query username , find matching password and then validate it with user_password and then send val result
	DECLARE var_userName varchar(30); 
    DECLARE var_userPswd  varchar(25);  
    DECLARE var_storeduserPswd varchar(25);
    -- DECLARE userCount varchar(10);
	 
	SET var_userName = user_Name;
    SET var_userPswd = user_Password; 
    

    -- Check if any of the input parameters are null
    IF var_userName IS NULL  OR var_userPswd IS NULL THEN
        SET ValidationResult = 'Invalid Input';
    ELSE
       -- check for sql injection 
			IF ( comp440_database_project.f_check_string_for_injection(var_userName) = 0)  THEN
				 SET ValidationResult = 'Injection Detected in User Name';
			ELSEIF (comp440_database_project.f_check_string_for_injection(var_userPswd) = 0)  THEN
				 SET ValidationResult = 'Injection Detected in User Password'; 
			ELSE
						   
			   -- QUERY db for username and fetch associated password and stored in var_storeduserPswd
					SELECT  userPassword
					INTO var_storeduserPswd 
					FROM comp440_database_project.userDetails
					WHERE userName = var_userName;
          
				-- Set the result based on the userCount
				IF var_storeduserPswd IS NOT NULL AND var_storeduserPswd = var_userPswd  THEN
					SET ValidationResult = 'User Exists';
				ELSEIF var_storeduserPswd IS NOT NULL AND var_storeduserPswd != var_userPswd  THEN
					SET ValidationResult = 'User Password Mismatch.';
				ELSE
					SET ValidationResult = 'User Does Not Exist';
				END IF;
			END IF;
          
    END IF;
    
    SELECT ValidationResult;
END$$
DELIMITER ;

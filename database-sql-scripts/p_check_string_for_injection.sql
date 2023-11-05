/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that can be called to check string for 
					sql injection through invoking the function f_check_string_for_injection
    Created By: Twishi Saran
    Updated On: 2023-10-08 17:00:01
    
    execution statement example: 
			call p_check_string_for_injection('create',@validationResult);
			select @validationResult;

*/

DELIMITER $$
USE  comp440_database_project$$
DROP PROCEDURE IF EXISTS p_check_string_for_injection$$
 

CREATE PROCEDURE p_check_string_for_injection (
									IN userName VARCHAR(30), 
									IN userPassword VARCHAR(25),
									IN user_firstName NVARCHAR(128),
									IN user_lastName NVARCHAR(128),
									IN user_emailID NVARCHAR(320),
                                    OUT validationResult INT)
BEGIN
	SET validationResult = 0;
    
    IF ( comp440_database_project.f_check_string_for_injection(userName) = 0)  THEN
        SET validationResult = 1;
    ELSEIF ( comp440_database_project.f_check_string_for_injection(userPassword) = 0)  THEN
		SET validationResult = 2;
	ELSEIF ( comp440_database_project.f_check_string_for_injection(user_firstName) = 0)  THEN
		SET validationResult = 3;
	ELSEIF ( comp440_database_project.f_check_string_for_injection(user_lastName) = 0)  THEN
		SET validationResult = 4;
	ELSEIF ( comp440_database_project.f_check_string_for_injection(user_emailID) = 0)  THEN
		SET validationResult = 5;
    END IF;
    
    select validationResult;
    
END$$
DELIMITER ;


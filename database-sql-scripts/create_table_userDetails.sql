/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that is called in UI to
					create the user details table  if it doesn't exist and
					if it exists, it will insert the new record into the table  to be used in  our project
    Created By: Twishi Saran
    Updated On: 2023-10-07 15:07:55
    
    execution statement example: 
			call save_userDetails ("userName","userPswd","userFname","userLName","userEmail", @outResult);

*/
DELIMITER $$
USE comp440_databse_project$$
DROP PROCEDURE IF EXISTS save_userDetails$$

CREATE PROCEDURE save_userDetails ( IN userName VARCHAR(30), 
									IN userPassword VARCHAR(25),
									IN user_firstName NVARCHAR(128),
									IN user_lastName NVARCHAR(128),
									IN user_emailID NVARCHAR(320),
                                    OUT record_insertion_status varchar(50)
                                    )
BEGIN
    DECLARE var_validationResult INT;
    SET var_validationResult = 0;
    
	CREATE TABLE IF NOT EXISTS `userDetails`(
		userName VARCHAR(30) NOT NULL PRIMARY KEY, 
        userPassword VARCHAR(25) NOT NULL,
        user_firstName NVARCHAR(128),
        user_lastName NVARCHAR(128),
        user_emailID NVARCHAR(320) UNIQUE        
		);
	 
	call p_check_string_for_injection(userName, userPassword, user_firstName, user_lastName, user_emailID , @validationResult);
    select  @validationResult  into var_validationResult;
  
    CASE
    WHEN var_validationResult = 0 THEN 
			INSERT INTO comp440_databse_project.userDetails (userName, userPassword,user_firstName,user_lastName,user_emailID)
					VALUES (userName,userPassword,user_firstName,user_lastName,user_emailID);
			SET record_insertion_status = 'Record Inserted';
    WHEN var_validationResult = 1 THEN 
		SET record_insertion_status = 'Injection Detected in Username'; 
    WHEN var_validationResult = 2 THEN 
		set record_insertion_status =  'Injection Detected in Password';
	WHEN var_validationResult = 3 THEN 
		SET record_insertion_status = 'Injection Detected in First Name'; 
	WHEN var_validationResult = 4 THEN 
		SET record_insertion_status = 'Injection Detected in Last Name'; 
	WHEN var_validationResult = 5 THEN 
		SET record_insertion_status = 'Injection Detected in Email ID'; 
    ELSE SET record_insertion_status = 'Record Not Inserted';
	END CASE;
    
    SELECT record_insertion_status;
     
END$$
DELIMITER ; 

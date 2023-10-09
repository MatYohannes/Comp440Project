/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a function that will check for sql injection in our project
    Created By: Twishi Saran
    Updated On: 2023-10-08 16:46:57
    
    execution statement example: 
			SELECT comp440_databse_project.f_check_string_for_injection('1=1') as ret_val; 

*/ 

DELIMITER $$
USE   comp440_databse_project$$
DROP FUNCTION IF EXISTS f_check_string_for_injection$$

CREATE FUNCTION f_check_string_for_injection (input_string VARCHAR(255)) 
		RETURNS INT DETERMINISTIC
BEGIN
    DECLARE ret_val INT;
	SET ret_val=1;
    
    IF (input_string like '%''%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%--%')  THEN SET ret_val=0; 
    ELSEIF (input_string like '%/*%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%*/%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%@')  THEN SET ret_val=0;
    ELSEIF (input_string like '%@@%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%char%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%nchar%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%varchar%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%nvarchar%')  THEN SET ret_val=0;
    
    ELSEIF (input_string like '%select%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%insert%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%update%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%delete%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%from%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%table%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%drop%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%create%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%alter%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%begin%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%end%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%grant%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%deny%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%exec%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%sp_%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%xp_%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%cursor%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%fetch%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%kill%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%open%')  THEN SET ret_val=0;
 
    ELSEIF (input_string like '%sysobjects%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%syscolumns%')  THEN SET ret_val=0;
	ELSEIF (input_string like '%1=1%')  THEN SET ret_val=0;
    ELSEIF (input_string like '%sys%')  THEN SET ret_val=0; 
	END IF;
    
    RETURN ret_val;
    
END$$
DELIMITER ;

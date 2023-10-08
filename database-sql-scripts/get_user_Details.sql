/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that is called in UI to
					get all the current user details in the database of our project
    Created By: Twishi Saran
    Updated On: 2023-10-07 17:22:22
    
    execution statement example: 
			call get_alluserDetails ();

*/

DELIMITER $$
USE comp440_databse_project$$
DROP PROCEDURE IF EXISTS get_all_userDetails$$

CREATE PROCEDURE get_alluserDetails ()
BEGIN

         SELECT userName as UserName,  
				CONCAT(user_firstName,' ',user_lastName) AS FullName,
                user_emailID as EmailID
		   FROM comp440_databse_project.userDetails
		ORDER BY FullName;

END$$
DELIMITER ;



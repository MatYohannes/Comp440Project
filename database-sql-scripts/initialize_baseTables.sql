/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that creates all the base tables to be used in the project
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call initialize_baseTables ();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS initialize_baseTables$$

CREATE PROCEDURE initialize_baseTables ()
BEGIN
   
    
	CREATE TABLE IF NOT EXISTS `userDetails`(
		userName VARCHAR(30) NOT NULL PRIMARY KEY, 
        userPassword VARCHAR(25) NOT NULL,
        user_firstName NVARCHAR(128),
        user_lastName NVARCHAR(128),
        user_emailID NVARCHAR(320) UNIQUE        
		);
	 
	
    
	CREATE TABLE IF NOT EXISTS `itemDetails`(
		itemID INT AUTO_INCREMENT PRIMARY KEY, 
		itemTitle VARCHAR(255),   
        itemDescription TEXT, 
        itemCategory VARCHAR(255),  
        itemPrice DECIMAL(10, 2),
        userName varchar(30),
        DateofListing date,
		foreign key (userName) references  userDetails(userName)        
		);
        
        
	CREATE TABLE IF NOT EXISTS `userReviews`(
		reviewID INT AUTO_INCREMENT PRIMARY KEY, 
		itemID INT,
        userReview VARCHAR(255),   
        userReviewDescription TEXT,  
        userName varchar(30),
        DateofReview date,
		foreign key (userName) references userDetails(userName),
        foreign key (itemID) references itemDetails(itemID),
		CONSTRAINT chk_userReview CHECK (userReview IN ('Excellent', 'Good', 'Fair', 'Poor'))
		);
	      
END$$
DELIMITER ; 

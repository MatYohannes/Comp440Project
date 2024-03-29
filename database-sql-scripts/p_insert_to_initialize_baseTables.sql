/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that inserts dummy data into all the base tables 
					to be used in the project while initializing the db
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call p_insert_to_initialize_baseTables ();

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_insert_to_initialize_baseTables$$

CREATE PROCEDURE p_insert_to_initialize_baseTables ()
BEGIN
	DECLARE minItemID INT;
    
	--   create tables
    CREATE TABLE IF NOT EXISTS `itemDetails`(
		itemID INT AUTO_INCREMENT, 
		itemTitle VARCHAR(255),   
        itemDescription VARCHAR(500), 
        itemCategory VARCHAR(255),  
        itemPrice DECIMAL(10, 2),
        userName varchar(30),
        DateofListing date,
        
        constraint fk_itemdetails_userName
		foreign key (userName) references userDetails(userName) ,
        PRIMARY KEY (itemID)
		);
        
	CREATE TABLE IF NOT EXISTS `userReviews`(
		reviewID INT AUTO_INCREMENT , 
		itemID INT,
        userReview VARCHAR(255),   
        userReviewDescription VARCHAR(500),  
        userName varchar(30),
        DateofReview date,
        
        
        constraint fk_userreview_userName
		foreign key (userName) references userDetails(userName) ,
        
        constraint fk_userreview_itemID
        foreign key (itemID) references itemDetails(itemID),
		CONSTRAINT chk_userReview CHECK (userReview IN ('Excellent', 'Good', 'Fair', 'Poor')),
        PRIMARY KEY (reviewID)
		);
	  
        
	INSERT INTO `comp440_database_project`.`itemDetails`(`itemTitle`,
														`itemDescription`,
														`itemCategory`,
														`itemPrice`,
														`userName`,
														`DateofListing`)
			VALUES 
            ('SAMSUNG Galaxy Z Fold 5 Cell Phone',
					'Android Smartphone 512GB with Big 7.6 Screen for Streaming, Gaming. Icy Blue.',
                    'electronics, cell phone, smartphone', 
					 218.20,    'Tsaran',  CURDATE()),
			('BANGSON Small Refridgerator',
  					'Small Refrigerator with Freezer, Silver.',
                      'electronics, home appliances, refridgerator', 279.99, 'Tsaran',CURDATE()),
			('Patio Heater for Outdoor Seating',
  					'Round Table Design, Double-Layer Stainless Steel Burner and Wheels, Outdoor Patio Heater',
                      'lawn and garden devices, outdoor cooling and heating, patio heater', 149.99, 'Tsaran', CURDATE()),
			('Portable Thermal Printer',
  					'Bluetooth Mini Pocket Printer Compatible with Android & iOS.',
                      'office supplies, office electronics, receipt printers', 49.99, 'Tsaran',CURDATE()),
			('Fitbit Charge 6 Smartwatch',
  					'Fitness Tracker with Google apps, Heart Rate on Exercise Equipment,Black, One Size.',
                      'electronics, wearable devices, smartwatch', 159.95, 'Tsaran',CURDATE())
			;
                  
	
    SELECT MIN(itemID) INTO minItemID FROM comp440_database_project.itemDetails;

    
  	INSERT INTO `comp440_database_project`.`userReviews` (`itemID`,
											`userReview`,
											`userReviewDescription`,
											`userName`,
											`DateofReview`)
  		 	VALUES 	 (minItemID,'Excellent','I love this phone. You can multitask in so many ways. GREAT BUY!','Tsaran',CURDATE()),
  					  (minItemID+1,'Good','Great for students and easy to install. Works quietly.','Tsaran',CURDATE()),
                      (minItemID+2,'Poor','Noisy and Difficult to assemble','Tsaran',CURDATE()),
                      (minItemID+3,'Fair','Easy to use and compatible with phone but ink dries up soon.','Tsaran',CURDATE()),
                      (minItemID+4,'Excellent','Great UI super easy to use and understand.','Tsaran',CURDATE())            
                  ;


END$$
DELIMITER ;
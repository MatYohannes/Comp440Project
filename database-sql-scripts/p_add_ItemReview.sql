/* 
	Project Name: COMP 440 Database Project - Group 5
    Script Details: This is the script will create a procedure that will let user write review for selected item 
    Created By: Twishi Saran
    Updated On:  2023-11-04 15:48:06
    
    execution statement example: 
			call p_add_ItemReview(ItemTitle, userReview, userReviewDescription, userReviewDate, ReviewerUserName, @output_message);
            select @output_message;

*/ 

DELIMITER $$
USE comp440_database_project$$
DROP PROCEDURE IF EXISTS p_add_ItemReview$$

-- Procedure to add a review for an item
CREATE PROCEDURE p_add_ItemReview(
  IN selectedItemTitle varchar(255),               
  IN userReview VARCHAR(255), 
  IN userReviewDescription VARCHAR(500)  ,
  IN userReviewDate DATE,
  IN ReviewerUserName varchar(30), 
  OUT output_message varchar(255)
)
BEGIN
  DECLARE review_count INT;
  DECLARE user_item_count INT;
  DECLARE reviewed_item_ID INT;
  DECLARE user_created_item INT;
  
  DECLARE EXIT HANDLER FOR SQLEXCEPTION  
        BEGIN
          SET output_message = 'Check Constraint Violation. Can only have review as Excellent/Good/Fair/Poor';
        END;
  
  -- Check if the user created the item
  SELECT COUNT(*) INTO user_created_item
	FROM itemDetails 
	WHERE userName = ReviewerUserName
	AND itemTitle = selectedItemTitle;

  IF user_created_item > 0 then 
		SET output_message = 'Cannot Add a review to the Item created by you';
  ELSE   
	 
     -- Check if the user has already reviewed 3 items today
	  SELECT COUNT(*) INTO user_item_count
		FROM userReviews 
	   WHERE userName  = ReviewerUserName
		 AND DateofReview  = userReviewDate;
		 
	  -- If user has reviewed their own item or exceeded daily review limit, exit
	  IF user_item_count >= 3 THEN 
		 SET output_message = 'Cannot exceed daily review limit of 3';
		
	  ELSE
		BEGIN
        
			 SELECT itemID INTO reviewed_item_ID
			   FROM itemDetails
			  WHERE itemTitle = selectedItemTitle;
			  
			-- Insert the review into the reviews table
			 INSERT INTO `comp440_database_project`.`userReviews` (`itemID`,
																	`userReview`,
																	`userReviewDescription`,
																	`userName`,
																	`DateofReview`)
				 VALUES (reviewed_item_ID, userReview, userReviewDescription, ReviewerUserName , userReviewDate);
                 
				 SET output_message = 'Review Inserted Successfully';
         END; 
	  END IF;
  END IF;
  
     select output_message;
END$$

DELIMITER ;
CREATE DATABASE IF NOT EXISTS USERS;
CREATE TABLE user_data
(  
    U_Id int(10) unsigned NOT NULL AUTO_INCREMENT,
    userEmail VARCHAR(255) DEFAULT NULL, 
    userPassword varchar(255) DEFAULT NULL,
    paymentType varchar(255) DEFAULT NULL,
    primary key (U_Id),
    UNIQUE KEY `userEmail` (`userEmail`)
);
INSERT INTO user_data(userEmail, userPassword,paymentType) VALUES ('jack@example.com', MD5('password'),'paypal');
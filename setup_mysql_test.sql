-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hcare_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON `hcare_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
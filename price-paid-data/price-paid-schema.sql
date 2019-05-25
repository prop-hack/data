-- Table structure for table `price_paid`
--
DROP TABLE IF EXISTS `price_paid`;
CREATE TABLE `price_paid` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `period` date NOT NULL,
  `price_paid` int NOT NULL,
  `postcode` char(8) NOT NULL,
  `postcode_geo` int UNSIGNED NOT NULL, -- link to postcode geo table, remove if not required
  `property_type` enum('D', 'S', 'T', 'F', 'O') NOT NULL,
  `new_build` enum('Y', 'N'),
  `estate_type` enum('F', 'L'),
  `name_number_1` varchar(50),
  `name_number_2` varchar(50),
  `street` varchar(100),
  `town_city` varchar(100),
  `district` varchar(100),
  `county` varchar(100),
  PRIMARY KEY(`id`),
  FOREIGN KEY (`postcode_geo`) REFERENCES postcode(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

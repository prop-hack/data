-- Table structure for table `area`
--
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `area_name` varchar(50) NOT NULL UNIQUE,
  `area_code` char(10) NOT NULL UNIQUE,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
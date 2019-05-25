-- Table structure for table `region`
--
DROP TABLE IF EXISTS `region`;
CREATE TABLE `region` (
  `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL UNIQUE,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
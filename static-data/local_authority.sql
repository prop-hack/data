-- Table structure for table `local_authority`
--
DROP TABLE IF EXISTS `local_authority`;
CREATE TABLE `local_authority` (
  `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL UNIQUE,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- Table structure for table `application_type`
--
DROP TABLE IF EXISTS `application_type`;
CREATE TABLE `application_type` (
  `id` smallint UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` char(7) NOT NULL UNIQUE,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table structure for table `application_by_region`
--
DROP TABLE IF EXISTS `applications_by_region`;
CREATE TABLE `applications_by_region` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `period` date NOT NULL,
  `region` varchar(30) NOT NULL UNIQUE,
  `type` smallint UNSIGNED NOT NULL,
  `amount` int UNSIGNED NOT NULL,
  PRIMARY KEY(`id`),
  FOREIGN KEY (type) REFERENCES application_type(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Table structure for table `applications_by_authority`
--
DROP TABLE IF EXISTS `applications_by_authority`;
CREATE TABLE `applications_by_authority` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `period` date NOT NULL,
  `authority` varchar(40) NOT NULL UNIQUE,
  `type` smallint UNSIGNED NOT NULL,
  `amount` int UNSIGNED NOT NULL,
  PRIMARY KEY(`id`),
  FOREIGN KEY (type) REFERENCES application_type(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

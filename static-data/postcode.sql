-- Table structure for table `postcode`
--
DROP TABLE IF EXISTS `postcode`;
CREATE TABLE `postcode` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `postcode` char(8) NOT NULL UNIQUE, -- with space postcode
  `outcode` char(4) NOT NULL, -- first portion of postcode
  `lat_long` POINT NOT NULL SRID 4326, -- lat/long
  `country` enum('England','Wales','Scotland','Northern Ireland','Channel Islands','Isle of Man') NOT NULL,
  PRIMARY KEY (`id`),
  SPATIAL INDEX(`lat_long`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
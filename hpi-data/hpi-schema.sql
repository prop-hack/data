-- Table structure for table `house_price_index`
--
DROP TABLE IF EXISTS `house_price_index`;
CREATE TABLE `house_price_index` (
  `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT,
  `period` date NOT NULL,
  `area` int UNSIGNED NOT NULL,
  `average_price` decimal(8, 2) NOT NULL,
  `index` float,
  `1m_change` float,
  `12m_change` float,
  `sales_volume` int,
  PRIMARY KEY(`id`),
  FOREIGN KEY (`area`) REFERENCES area(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
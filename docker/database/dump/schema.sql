CREATE DATABASE testDB;

use testDB;

CREATE TABLE IF NOT EXISTS `cart` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(36) NOT NULL,
  `checked_out` tinyint(1) DEFAULT 0,
  `user_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(36) NOT NULL,
  `final_price` int(10) unsigned NOT NULL DEFAULT 0,
  `final_price_decimals` int(2) unsigned NOT NULL DEFAULT 2,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `element` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(36) NOT NULL,
  `cart_id` int(10) unsigned,
  `product_id` int(10) unsigned,
  `name` varchar(64),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `order_element` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(36) NOT NULL,
  `order_id` int(10) unsigned,
  `product_id` int(10) unsigned,
  `name` varchar(64),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `discount` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cart_id` int(10) unsigned DEFAULT NULL,
  `order_id` int(10) unsigned,
  `code` varchar(20) NOT NULL,
  `percentage` int(4) unsigned NOT NULL DEFAULT 0,
  `decimals` int(2) unsigned NOT NULL DEFAULT 2,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `product` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `reference` varchar(20) NOT NULL,
  `name`  varchar(20) NOT NULL,
  `price` int(10) unsigned NOT NULL DEFAULT 0,
  `decimals` int(2) unsigned NOT NULL DEFAULT 2,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


INSERT INTO `product` VALUES
(1, 'PROD_1', 'Xbox One S', 30000, 2),
(2, 'PROD_2', 'Xbox One X', 40000, 2),
(3, 'PROD_3', 'PlayStation 4 Slim', 35000, 2),
(4, 'PROD_4', 'PlayStation 4 Pro', 45000, 2),
(5, 'PROD_5', 'Nintendo Wii', 10000, 2),
(6, 'PROD_6', 'Nintendo Switch', 25000, 2),
(7, 'PROD_7', 'Dreamcast', 5000, 2),
(8, 'PROD_8', 'Sega Saturn', 7500, 2),
(9, 'PROD_9', 'Sega Megadrive 2', 7000, 2);

INSERT INTO `discount` VALUES
(1, null, null, 'GREATDEAL', 5000, 2),
(2, null, null, 'HOTDEAL10', 1000, 2);


GRANT ALL PRIVILEGES ON testDB.* TO testuser;



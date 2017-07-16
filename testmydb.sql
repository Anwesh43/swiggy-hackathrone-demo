-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 16, 2017 at 03:38 AM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `testmydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE IF NOT EXISTS `order_details` (
  `order_id` bigint(20) NOT NULL,
  `ordered_time` datetime DEFAULT NULL,
  `payment_status` varchar(100) DEFAULT NULL,
  `customer_id` int(50) DEFAULT NULL,
  `customer_lat` varchar(50) DEFAULT NULL,
  `customer_lng` varchar(50) DEFAULT NULL,
  `customer_user_agent` varchar(50) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `restaurant_id` int(11) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `restaurant_id` (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`order_id`, `ordered_time`, `payment_status`, `customer_id`, `customer_lat`, `customer_lng`, `customer_user_agent`, `payment_method`, `restaurant_id`) VALUES
(1, NULL, '0', 1, '0', '0', 'User Agent 1', 'Swiggy Bank', 1),
(2, '2017-07-16 00:00:00', '0', 0, '0', '0', 'User Agent 1', 'Swiggy Bank', 6940798),
(3, '2017-07-16 00:00:00', '0', 0, '0', '0', 'User Agent 1', 'Swiggy Bank', 6940798);

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE IF NOT EXISTS `order_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` bigint(20) DEFAULT NULL,
  `item_id` bigint(20) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `item_id` (`item_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`id`, `order_id`, `item_id`, `quantity`) VALUES
(43, 2, 1, 1),
(44, 2, 2, 1),
(45, 2, 3, 1),
(46, 3, 1, 1),
(47, 3, 2, 1),
(48, 3, 3, 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

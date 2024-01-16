-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 02:09 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kpop_site`
--

-- --------------------------------------------------------

--
-- Table structure for table `cust_details`
--

CREATE TABLE `cust_details` (
  `cust_name` varchar(30) NOT NULL,
  `cust_email` varchar(30) NOT NULL,
  `cust_phone` bigint(12) NOT NULL,
  `membership_id` varchar(6) NOT NULL,
  `total_ticket` int(3) NOT NULL,
  `TOTAL` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cust_details`
--

INSERT INTO `cust_details` (`cust_name`, `cust_email`, `cust_phone`, `membership_id`, `total_ticket`, `TOTAL`) VALUES
('Nurul Syakirah', 'ira@gmail.com', 601123454837, 'R1G9K', 2, 100),
('Alia Sofea', 'alia@gmail.com', 60112385745, '2HHKH', 1, 50),
('Ameera Nafeesa', 'nana@gmail.com', 60142345726, 'QCOPB', 3, 135),
('Hani Rasyiqah Irdina', 'hani@gmail.com', 60115726348, 'KQM4U', 5, 225);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

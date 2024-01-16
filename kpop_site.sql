-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 11:55 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `fm_details`
--

CREATE TABLE `fm_details` (
  `Ticket_ID` varchar(8) NOT NULL,
  `Name` char(100) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Membership_ID` varchar(5) NOT NULL,
  `Number_of_Tickets` int(1) NOT NULL,
  `Total_Cost` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fm_details`
--

INSERT INTO `fm_details` (`Ticket_ID`, `Name`, `Email`, `Membership_ID`, `Number_of_Tickets`, `Total_Cost`) VALUES
('O8KRIG', 'Nurul Syakirah', 'ira@gmail.com', 'R1G9K', 1, 150),
('W0I9I3', 'Alia Sofea', 'alia@gmail.com', '2HHKH', 4, 600),
('DXDBOJ', 'Ameera Nafeesa', 'nana@gmail.com', 'QCOPB', 2, 300),
('MIR1LL', 'Hani Rasyiqah Irdina', 'hani@gmail.com', 'KQM4U', 3, 450);

-- --------------------------------------------------------

--
-- Table structure for table `memship_details`
--

CREATE TABLE `memship_details` (
  `member_ID` varchar(6) NOT NULL,
  `user_name` text NOT NULL,
  `user_dob` date NOT NULL,
  `user_age` int(3) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_phone` bigint(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `memship_details`
--

INSERT INTO `memship_details` (`member_ID`, `user_name`, `user_dob`, `user_age`, `user_email`, `user_phone`) VALUES
('R1G9K', 'Nurul Syakirah', '2004-12-10', 19, 'ira@gmail.com', 6011332273847),
('2HHKH', 'Alia Sofea', '2004-06-10', 19, 'aliasofea@gmail.com', 60112385745),
('QCOPB', 'Ameera Nafeesa', '2004-03-20', 19, 'nana@gmail.com', 60142345726),
('KQM4U', 'Hani Rasyiqah Irdina', '2004-01-23', 19, 'hani@gmail.com', 60115726348);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

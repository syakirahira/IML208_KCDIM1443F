-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 02:10 PM
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

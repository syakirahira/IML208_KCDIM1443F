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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

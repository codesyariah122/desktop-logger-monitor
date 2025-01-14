-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 14, 2025 at 03:55 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `activity_log`
--

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `app_usage_time` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`app_usage_time`)),
  `keyboard_usage` decimal(10,2) NOT NULL,
  `mouse_usage` decimal(10,2) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `email`, `app_usage_time`, `keyboard_usage`, `mouse_usage`, `created_at`) VALUES
(5, 'pujiermanto@gmail.com', '{\"\\u25cf import requests \\u2022 Untitled-1 - python-project - Visual Studio Code\": 6, \"\\u25cf asdsakdjasdasdasdjhasdasjdasdasd \\u2022 Untitled-2 - python-project - Visual Studio Code\": 2, \"Task Switching\": 13, \"Enter Email\": 4, \"python\": 30, \"ChatGPT \\u2014 Mozilla Firefox\": 3, \"(9) The Strokes - OBLIVIUS (Official Lyric Video) - YouTube - Google Chrome\": 16, \"(9) seringai pulang - YouTube - Google Chrome\": 6, \"(9) Pulang - YouTube - Google Chrome\": 15, \"(9) Dilarang Di Bandung - YouTube - Google Chrome\": 9, \"mouse-keybord-logger.py - python-project - Visual Studio Code\": 7, \"Untitled-2 - python-project - Visual Studio Code\": 3, \"\\u25cf save_d \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf save_data_to \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf save_data_to_db \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf save_data_to_db() \\u2022 Untitled-2 - python-project - Visual Studio Code\": 5, \"\\u25cf def save_data_to_db() \\u2022 Untitled-2 - python-project - Visual Studio Code\": 37, \"Save As\": 12, \"\\u25cf asdsa \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf asdsadkasjdaskdjqwkjekwq \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf asdsadkasjdaskdjqwkjekwqjekqwjekqwjeklqw \\u2022 Untitled-2 - python-project - Visual Studio Code\": 26, \"backup-logger2.py - python-project - Visual Studio Code\": 10, \"README.md - python-project - Visual Studio Code\": 2, \"\\u25cf sad \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf sadahsdjhasjkdhasjkhdasjkdhas \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf sadahsdjhasjkdhasjkhdasjkdhasdh \\u2022 Untitled-2 - python-project - Visual Studio Code\": 11, \"\\u25cf d \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf dasjhdjkashdjkashdkjash \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkdasdas \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkdasdasjkdhasjdkhaswqm,enqw \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkdasdasjkdhasjdkhaswqm,enqweqwe,qwmckxz \\u2022 Untitled-2 - python-project - Visual Studio Code\": 3, \"\\u25cf jkL \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkLkZjkl \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkLkZjkljkljklKLJ \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkLkZjkljkljklKLJkk \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkLkZjkljkljklKLJkkjkjksajdklasd \\u2022 Untitled-2 - python-project - Visual Studio Code\": 1, \"\\u25cf jkLkZjkljkljklKLJkkjkjksajdklasdkljsadka \\u2022 Untitled-2 - python-project - Visual Studio Code\": 26}', 4.00, 0.00, '2025-01-14 03:53:28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

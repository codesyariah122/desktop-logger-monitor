-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2025 at 04:12 AM
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
  `keyboard_usage` decimal(8,2) NOT NULL,
  `mouse_usage` decimal(8,2) NOT NULL,
  `device` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `email`, `app_usage_time`, `keyboard_usage`, `mouse_usage`, `device`, `created_at`) VALUES
(9, 'pujiermanto@gmail.com', '{\"Enter Email\":45,\"Activity Usage | PM Tokoweb\":524,\"activity-monitor.py - python-project - Visual Studio Code\":164,\"(9) WhatsApp \\u2014 Mozilla Firefox\":5,\"Task Switching\":176,\"(8) WhatsApp \\u2014 Mozilla Firefox\":10,\"localhost \\/ 127.0.0.1 \\/ activity_log \\/ log | phpMyAdmin 5.2.1 \\u2014 Mozilla Firefox\":208,\"System tray overflow window.\":48,\"Tabel data kosong penanganan \\u2014 Mozilla Firefox\":100,\"LogController.php - send-activity - Visual Studio Code\":111,\"ActivityService.php - send-activity - Visual Studio Code\":21,\"EmailController.php - send-activity - Visual Studio Code\":1032,\"LogService.php - send-activity - Visual Studio Code\":846,\"\\u25cf LogService.php - send-activity - Visual Studio Code\":54,\"EmailService.php - send-activity - Visual Studio Code\":1447,\"\\u25cf EmailService.php - send-activity - Visual Studio Code\":540,\"DatabaseSecondary.php - send-activity - Visual Studio Code\":318,\"Kirim Data ke API \\u2014 Mozilla Firefox\":7405,\"ChatGPT \\u2014 Mozilla Firefox\":37,\"\\u25cf EmailController.php - send-activity - Visual Studio Code\":1058,\"localhost \\/ 127.0.0.1 \\/ u1643812_pm | phpMyAdmin 5.2.1 \\u2014 Mozilla Firefox\":127,\"localhost \\/ 127.0.0.1 \\/ u1643812_pm \\/ _users | phpMyAdmin 5.2.1 \\u2014 Mozilla Firefox\":407,\"index.php - send-activity - Visual Studio Code\":197,\"\\u25cf index.php - send-activity - Visual Studio Code\":921,\"Mozilla Firefox\":207,\"http:\\/\\/localhost:9091\\/api\\/get-log.php?email=pujiermanto@gmail.com \\u2014 Mozilla Firefox\":151,\"http:\\/\\/localhost:9091\\/api\\/user-data?email=pujiermanto@gmail.com \\u2014 Mozilla Firefox\":144,\"http:\\/\\/localhost:9091\\/api\\/logs?email=pujiermanto@gmail.com \\u2014 Mozilla Firefox\":27,\"python\":13}', 4.38, 6.46, 'Device: DESKTOP-452UK2F, System: Windows, Processor: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel, Architecture: AMD64', '2025-01-15 16:56:15'),
(12, 'pujiermanto@gmail.com', '{\"Enter Email\":504,\"activity-monitor.py - python-project - Visual Studio Code\":1900,\"Task Switching\":141,\"Tabel data kosong penanganan \\u2014 Mozilla Firefox\":3298,\"Mozilla Firefox\":92,\"http:\\/\\/localhost:9091\\/api\\/logs?email=pujiermanto@gmail.com - Error \\u2014 Mozilla Firefox\":21,\"System tray overflow window.\":23,\"XAMPP Control Panel v3.3.0   [ Compiled: Apr 6th 2021 ]\":77,\"http:\\/\\/localhost:9091\\/api\\/logs?email=pujiermanto@gmail.com \\u2014 Mozilla Firefox\":149,\"Activity Usage | PM Tokoweb\":277,\"http:\\/\\/localhost:9091\\/api\\/user-data?email=pujiermanto@gmail.com \\u2014 Mozilla Firefox\":39,\"\\u25cf activity-monitor.py - python-project - Visual Studio Code\":1306,\"python\":12}', 1.24, 0.65, 'Device: DESKTOP-452UK2F, System: Windows, Processor: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel, Architecture: AMD64', '2025-01-15 17:41:03'),
(36, 'pujiermanto@gmail.com', '{\"Enter Email\":87,\"System tray overflow window.\":47,\"XAMPP Control Panel v3.3.0   [ Compiled: Apr 6th 2021 ]\":80,\"Activity Usage | PM Tokoweb\":431,\"activity-monitor.py - python-project - Visual Studio Code\":455,\"Task Switching\":202,\"ChatGPT \\u2014 Mozilla Firefox\":1400,\"DatabaseSecondary.php - send-activity - Visual Studio Code\":73,\"index.php - send-activity - Visual Studio Code\":77,\"Database.php - send-activity - Visual Studio Code\":35,\"LogController.php - send-activity - Visual Studio Code\":54,\"LogService.php - send-activity - Visual Studio Code\":136,\"404 Not Found - Google Chrome\":51,\"cPanel File Manager v3 - Google Chrome\":225,\"index.php - cPanel File Manager v3 - Google Chrome\":18,\"Untitled - Google Chrome\":5,\".htaccess - cPanel File Manager v3 - Google Chrome\":55,\"pm-activity.tokoweb.live\\/api\\/check-email?email=pujiermanto@gmail.com - Google Chrome\":282,\"pm-activity.tokoweb.live\":20,\"pm-activity.tokoweb.live\\/api\\/user-data?email=pujiermanto@gmail.com - Google Chrome\":308,\"cPanel - Manage My Databases - Google Chrome\":45,\"cPanel - Domains - Google Chrome\":99,\"(12) WhatsApp \\u2014 Mozilla Firefox\":26,\"(11) WhatsApp \\u2014 Mozilla Firefox\":967,\"(10) WhatsApp \\u2014 Mozilla Firefox\":58,\"python\":11}', 0.77, 0.57, 'Device: DESKTOP-452UK2F, System: Windows, Processor: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel, Architecture: AMD64', '2025-01-16 04:09:37');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

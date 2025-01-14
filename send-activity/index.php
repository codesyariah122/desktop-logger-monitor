<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return filesystem
 */
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');
// Fungsi untuk mengambil data log berdasarkan email
require_once __DIR__ . '/vendor/autoload.php';

use App\Controllers\{LogController, EmailController};

$requestUri = $_SERVER['REQUEST_URI'];
$emailController = new EmailController();
$logController = new LogController();

if (strpos($requestUri, '/api/check-email') !== false) {
    require_once __DIR__ . '/vendor/autoload.php';
    $emailController->checkEmail();
} else if (strpos($requestUri, '/api/logs') !== false) {
    require_once __DIR__ . '/vendor/autoload.php';

    $logController->handleRequest();
} else if (strpos($requestUri, '/api/send-activity') !== false) {
    $logController->sendActivity();
} else {
    http_response_code(404);
    echo json_encode([
        'status' => 'error',
        'message' => 'Not Found'
    ], JSON_PRETTY_PRINT);
}

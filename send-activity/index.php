<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return loader
 */

ini_set('display_errors', 1);
error_reporting(E_ALL);

require_once __DIR__ . '/vendor/autoload.php';

use App\Controllers\{LogController, EmailController};

$requestUri = $_SERVER['REQUEST_URI'];
$emailController = new EmailController();
$logController = new LogController();

if (strpos($requestUri, '/download-page') !== false) {
    $logController->showDownloadPage();
} else {
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
    header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
    header('Content-Type: application/json');
    if (strpos($requestUri, '/api/check-email') !== false) {
        $emailController->checkEmail();
    } else if (strpos($requestUri, '/api/logs') !== false) {
        $logController->handleRequest();
    } else if (strpos($requestUri, '/api/send-activity') !== false) {
        $logController->sendActivity();
    } else if (strpos($requestUri, '/api/user-data') !== false) {
        $emailController->handleUserData();
    } else if (strpos($requestUri, '/download-file') !== false) {
        $logController->downloadFile();
    } else {
        http_response_code(404);
        echo json_encode([
            'status' => 'error',
            'message' => 'Not Found'
        ], JSON_PRETTY_PRINT);
    }
}

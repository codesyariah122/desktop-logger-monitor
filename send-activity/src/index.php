<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return generic
 */

namespace App\Server;

require_once __DIR__ . '/../vendor/autoload.php';

use App\Controllers\{LogController, EmailController};
use App\Config\{HeadersSet};

class AgoGoConnect
{
    public static function go()
    {
        $requestUri = $_SERVER['REQUEST_URI'];
        $emailController = new EmailController();
        $logController = new LogController();
        $header = new HeadersSet();

        if (strpos($requestUri, '/download-page') !== false) {
            $logController->showDownloadPage();
        } else {
            $header::runHeader('api');
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
    }
}

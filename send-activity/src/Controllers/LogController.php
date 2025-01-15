<?php

namespace App\Controllers;

use App\Services\{LogService, ActivityService};

class LogController
{
    private $logService, $activityService;

    public function __construct()
    {
        $this->logService = new LogService();
        $this->activityService = new ActivityService();
    }

    public function handleRequest()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'GET') {
            $email = $_GET['email'] ?? null;
            $response = $this->logService->getLogs($email);

            header('Content-Type: application/json');
            echo json_encode($response, JSON_PRETTY_PRINT);
        } else {
            http_response_code(405);
            echo json_encode([
                'status' => 'error',
                'message' => 'Only GET method is allowed.'
            ], JSON_PRETTY_PRINT);
        }
    }

    public function sendActivity()
    {
        // Hanya izinkan metode POST
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            http_response_code(405);
            echo json_encode([
                'status' => 'error',
                'message' => 'Only POST method is allowed.'
            ]);
            exit;
        }

        // Ambil data dari POST
        $email = isset($_POST['email']) ? trim($_POST['email']) : null;
        $app_usage_time = isset($_POST['app_usage_time']) ? $_POST['app_usage_time'] : null;
        $keyboard_usage = isset($_POST['keyboard_usage']) ? intval($_POST['keyboard_usage']) : null;
        $mouse_usage = isset($_POST['mouse_usage']) ? intval($_POST['mouse_usage']) : null;

        // Validasi input
        if (empty($email) || empty($app_usage_time) || $keyboard_usage === null || $mouse_usage === null) {
            http_response_code(400); // Bad request
            echo json_encode([
                'status' => 'error',
                'message' => 'Invalid input. All fields are required.'
            ]);
            exit;
        }

        // Decode JSON untuk app_usage_time (validasi tambahan)
        $app_usage_time_decoded = json_decode($app_usage_time, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            http_response_code(400); // Bad request
            echo json_encode([
                'status' => 'error',
                'message' => 'Invalid JSON format for app_usage_time.'
            ]);
            exit;
        }

        // Siapkan data untuk service
        $data = [
            'email' => $email,
            'app_usage_time' => $app_usage_time_decoded,
            'keyboard_usage' => $keyboard_usage,
            'mouse_usage' => $mouse_usage,
            'created_at' => date('Y-m-d H:i:s'),
        ];

        $response = $this->activityService->processActivity($data);

        // Tampilkan respons dari service
        http_response_code($response['status'] === 'success' ? 200 : 500);
        echo json_encode($response, JSON_PRETTY_PRINT);
    }
}

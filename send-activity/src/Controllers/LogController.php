<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

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
        $datetime = new \DateTime('now', new \DateTimeZone('Asia/Jakarta'));

        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            http_response_code(405);
            echo json_encode([
                'status' => 'error',
                'message' => 'Only POST method is allowed.'
            ]);
            exit;
        }

        $email = isset($_POST['email']) ? trim($_POST['email']) : null;
        $location = isset($_POST['location']) ? $_POST['location'] : null;
        $app_usage_time = isset($_POST['app_usage_time']) ? $_POST['app_usage_time'] : null;
        $keyboard_usage = isset($_POST['keyboard_usage']) ? floatval($_POST['keyboard_usage']) : null;
        $mouse_usage = isset($_POST['mouse_usage']) ? floatval($_POST['mouse_usage']) : null;
        $device = isset($_POST['device']) ? $_POST['device'] : null;

        if (empty($email) || empty($location) || empty($app_usage_time) || $keyboard_usage === null || $mouse_usage === null || $device === null) {
            http_response_code(400);
            echo json_encode([
                'status' => 'error',
                'message' => 'Invalid input. All fields are required.'
            ]);
            exit;
        }

        $app_usage_time_decoded = json_decode($app_usage_time, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            http_response_code(400);
            echo json_encode([
                'status' => 'error',
                'message' => 'Invalid JSON format for app_usage_time.'
            ]);
            exit;
        }

        $data = [
            'email' => $email,
            'location' => $location,
            'app_usage_time' => $app_usage_time_decoded,
            'keyboard_usage' => $keyboard_usage,
            'mouse_usage' => $mouse_usage,
            'device' => $device,
            // 'created_at' => date('Y-m-d H:i:s'),
            'created_at' => $datetime->format('Y-m-d H:i:s')
        ];

        $response = $this->activityService->processActivity($data);

        http_response_code($response['status'] === 'success' ? 200 : 500);
        echo json_encode($response, JSON_PRETTY_PRINT);
    }

    public function downloadFile()
    {
        try {
            // Ambil User-Agent dari perangkat klien
            $userAgent = $_SERVER['HTTP_USER_AGENT'];

            // Deteksi sistem operasi berdasarkan User-Agent
            if (stripos($userAgent, 'Windows') !== false) {
                $filePath = __DIR__ . '/../storage/devices/windows/PMTokowebActivityUsage.exe';
            } elseif (stripos($userAgent, 'Macintosh') !== false || stripos($userAgent, 'Mac OS X') !== false) {
                header('Content-Type: text/html; charset=UTF-8');
                http_response_code(200);
                echo '
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
                </head>
                <body>
                    <script>
                        Swal.fire({
                            title: "Informasi",
                            text: "Untuk pengguna Mac OS X, aplikasi sedang dipersiapkan oleh administrator.",
                            icon: "info",
                            confirmButtonText: "Kembali"
                        }).then((result) => {
                            if (result.isConfirmed) {
                                window.history.back();
                            }
                        });
                    </script>
                </body>
                </html>
            ';
                exit;
            } else {
                http_response_code(400);
                echo json_encode([
                    'status' => 'error',
                    'message' => 'Unsupported operating system.',
                    'user_agent' => $userAgent
                ], JSON_PRETTY_PRINT);
                exit;
            }

            // Lakukan proses download jika file ditemukan
            if (file_exists($filePath)) {
                header('Content-Description: File Transfer');
                header('Content-Type: application/octet-stream');
                header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
                header('Expires: 0');
                header('Cache-Control: must-revalidate');
                header('Pragma: public');
                header('Content-Length: ' . filesize($filePath));
                readfile($filePath);
                exit;
            } else {
                http_response_code(404);
                echo json_encode([
                    'status' => 'error',
                    'message' => 'File not found.'
                ], JSON_PRETTY_PRINT);
            }
        } catch (\Exception $e) {
            echo $e->getMessage();
        }
    }


    public function showDownloadPage()
    {
        $viewPath = __DIR__ . '/../Views/download.php';
        if (file_exists($viewPath)) {
            include $viewPath;
        } else {
            http_response_code(404);
            echo json_encode([
                'status' => 'error',
                'message' => 'View not found.'
            ], JSON_PRETTY_PRINT);
        }
    }
}

<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Services;

use App\Config\{Database, DatabaseSecondary};
use PDO;
use PDOException;

class LogService
{
    private $pdo;

    public function __construct()
    {
        $this->pdo = Database::getInstance()->getConnection();
    }

    public function getLogs($email = null): array
    {
        try {
            $query = "SELECT * FROM log";
            if ($email) {
                $query .= " WHERE email = :email";
            }

            $stmt = $this->pdo->prepare($query);
            if ($email) {
                $stmt->bindParam(':email', $email);
            }

            $stmt->execute();
            $logs = $stmt->fetchAll(PDO::FETCH_ASSOC);

            foreach ($logs as &$log) {
                if (isset($log['app_usage_time'])) {
                    $log['app_usage_time'] = json_decode($log['app_usage_time'], true);

                    // Cari aplikasi dengan durasi terlama
                    $maxApp = null;
                    $maxTime = 0;
                    $totalTime = 0;

                    foreach ($log['app_usage_time'] as $app => $time) {
                        $totalTime += $time;
                        if ($time > $maxTime) {
                            $maxApp = $app;
                            $maxTime = $time;
                        }
                    }

                    // Hitung persentase durasi waktu terlama
                    $percentage = $totalTime > 0 ? round(($maxTime / $totalTime) * 100, 2) : 0;

                    // Tambahkan informasi aplikasi terlama ke log
                    $log['longest_app'] = [
                        'app_name' => $maxApp,
                        'duration' => ceil($maxTime / 3600),
                        'percentage' => $percentage,
                    ];
                }
            }

            return [
                'status' => 'success',
                'data' => $logs ?: 'No records found.',
            ];
        } catch (PDOException $e) {
            return [
                'status' => 'error',
                'message' => 'Database error: ' . $e->getMessage(),
            ];
        }
    }
}

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

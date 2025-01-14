<?php

namespace App\Services;

use App\Database;
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

    public function checkEmailExistsInSecondDatabase($email): bool
    {
        try {
            // Konfigurasi database kedua
            $host = '127.0.0.1';
            $dbname = 'u1643812_pm';  // Nama database kedua
            $username = 'root';
            $password = '';

            // Koneksi ke database kedua
            $pdoSecondDb = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
            $pdoSecondDb->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Query untuk mengecek apakah email ada
            $stmt = $pdoSecondDb->prepare("SELECT 1 FROM _users WHERE email = :email LIMIT 1");
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            // Jika email ditemukan, kembalikan true
            return $stmt->rowCount() > 0;
        } catch (PDOException $e) {
            // Jika terjadi error, return false
            return false;
        }
    }
}

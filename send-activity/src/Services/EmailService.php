<?php

namespace App\Services;

use App\Config\{Database, DatabaseSecondary};
use PDO;
use PDOException;

class EmailService
{
    private $pdo;

    public function __construct()
    {
        $this->pdo = DatabaseSecondary::getInstance()->getConnection();
    }

    public function checkEmailExistsInSecondDatabase($email): bool
    {
        try {
            $stmt = $this->pdo->prepare("SELECT 1 FROM _users WHERE email = :email LIMIT 1");
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            return $stmt->rowCount() > 0;
        } catch (PDOException $e) {
            return false;
        }
    }

    public function getUserDataByEmail($email)
    {
        try {
            $stmt = $this->pdo->prepare("SELECT id, first_name, last_name, image, job_title FROM _users WHERE email = :email LIMIT 1");
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            $userData = $stmt->fetch(PDO::FETCH_ASSOC);

            return $userData ? $userData : null;
        } catch (PDOException $e) {
            return null;
        }
    }

    // public function getAttendanceDataByUserId($userId)
    // {
    //     try {
    //         $stmt = $this->pdo->prepare(
    //             "SELECT * FROM _attendance WHERE user_id = :user_id AND out_time IS NULL AND DATE(in_time) = CURDATE()"
    //         );
    //         $stmt = $this->pdo->prepare(
    //             "SELECT * FROM _attendance WHERE user_id = :user_id AND out_time IS NULL"
    //         );
    //         // Perbandingan tanggal di kedua sisi
    //         $stmt = $this->pdo->prepare(
    //             "SELECT * FROM _attendance WHERE user_id = :user_id AND out_time IS NULL AND DATE(in_time) = DATE(NOW())"
    //         );
    //         $stmt->bindParam(':user_id', $userId);
    //         $stmt->execute();

    //         $attendanceData = $stmt->fetchAll(PDO::FETCH_ASSOC);

    //         return $attendanceData ? $attendanceData : [];
    //     } catch (PDOException $e) {
    //         return [];
    //     }
    // }

    public function getAttendanceDataByUserId($userId)
    {
        try {
            $stmt = $this->pdo->prepare(
                // Ambil semua attendance hari ini (boleh sudah out atau belum)
                "SELECT * FROM _attendance WHERE user_id = :user_id AND DATE(in_time) = DATE(NOW())"
            );
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();

            $attendanceData = $stmt->fetchAll(PDO::FETCH_ASSOC);

            return $attendanceData ? $attendanceData : [];
        } catch (PDOException $e) {
            return [];
        }
    }
}

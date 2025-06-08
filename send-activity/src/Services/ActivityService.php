<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Services;

use App\Config\{Database, DatabaseSecondary};
use PDO;
use PDOException;

class ActivityService
{
    private $pdo;

    public function __construct()
    {
        $this->pdo = Database::getInstance()->getConnection();
    }

    public function processActivity($data)
    {
        try {
            // Ambil tanggal saja dari created_at untuk perbandingan
            $created_date = date('Y-m-d', strtotime($data['created_at']));

            // Cek apakah data sudah ada di database
            $queryCheck = "SELECT COUNT(*) as count 
                       FROM log 
                       WHERE email = :email AND device = :device AND DATE(created_at) = :created_date";

            $stmtCheck = $this->pdo->prepare($queryCheck);
            $stmtCheck->bindParam(':email', $data['email']);
            $stmtCheck->bindParam(':device', $data['device']);
            $stmtCheck->bindParam(':created_date', $created_date);
            $stmtCheck->execute();
            $result = $stmtCheck->fetch(PDO::FETCH_ASSOC);

            if ($result['count'] > 0) {
                // Jika data sudah ada, lakukan UPDATE
                $queryUpdate = "UPDATE log 
                            SET app_usage_time = :app_usage_time, 
                                keyboard_usage = :keyboard_usage, 
                                mouse_usage = :mouse_usage,
                                location = :location
                            WHERE email = :email AND device = :device AND DATE(created_at) = :created_date";

                $stmtUpdate = $this->pdo->prepare($queryUpdate);
                $appUsageTimeJson = json_encode($data['app_usage_time']);
                $stmtUpdate->bindParam(':app_usage_time', $appUsageTimeJson);
                $stmtUpdate->bindParam(':keyboard_usage', $data['keyboard_usage']);
                $stmtUpdate->bindParam(':mouse_usage', $data['mouse_usage']);
                $stmtUpdate->bindParam(':email', $data['email']);
                $stmtUpdate->bindParam(':location', $data['location']);
                $stmtUpdate->bindParam(':device', $data['device']);
                $stmtUpdate->bindParam(':created_date', $created_date);

                $stmtUpdate->execute();

                return [
                    'status' => 'success',
                    'message' => 'Activity data updated successfully.'
                ];
            } else {
                // Jika data belum ada, lakukan INSERT
                $queryInsert = "INSERT INTO log (email, location, app_usage_time, keyboard_usage, mouse_usage, device, created_at) 
                            VALUES (:email, :location, :app_usage_time, :keyboard_usage, :mouse_usage, :device, :created_at)";

                $stmtInsert = $this->pdo->prepare($queryInsert);
                $app_usage_time = json_encode($data['app_usage_time']);
                $stmtInsert->bindParam(':email', $data['email']);
                $stmtInsert->bindParam(':location', $data['location']);
                $stmtInsert->bindParam(':app_usage_time', $app_usage_time);
                $stmtInsert->bindParam(':keyboard_usage', $data['keyboard_usage']);
                $stmtInsert->bindParam(':mouse_usage', $data['mouse_usage']);
                $stmtInsert->bindParam(':device', $data['device']);
                $stmtInsert->bindParam(':created_at', $data['created_at']);

                $stmtInsert->execute();

                return [
                    'status' => 'success',
                    'message' => 'Activity data saved successfully.'
                ];
            }
        } catch (PDOException $e) {
            return [
                'status' => 'error',
                'message' => 'Database error: ' . $e->getMessage()
            ];
        }
    }
}

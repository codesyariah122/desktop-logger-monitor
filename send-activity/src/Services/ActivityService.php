<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Services;

use App\Database;
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
            $query = "INSERT INTO log (email, app_usage_time, keyboard_usage, mouse_usage, device, created_at) 
                  VALUES (:email, :app_usage_time, :keyboard_usage, :mouse_usage, :device, :created_at)";

            $stmt = $this->pdo->prepare($query);

            // Buat variabel untuk setiap nilai
            $email = $data['email'];
            $app_usage_time = json_encode($data['app_usage_time']);
            $keyboard_usage = $data['keyboard_usage'];
            $mouse_usage = $data['mouse_usage'];
            $device = $data['device'];
            $created_at = $data['created_at'];

            // Bind data ke query
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':app_usage_time', $app_usage_time);
            $stmt->bindParam(':keyboard_usage', $keyboard_usage);
            $stmt->bindParam(':mouse_usage', $mouse_usage);
            $stmt->bindParam(':device', $device);
            $stmt->bindParam(':created_at', $created_at);

            // Eksekusi query
            $stmt->execute();

            return [
                'status' => 'success',
                'message' => 'Activity data saved successfully.'
            ];
        } catch (PDOException $e) {
            return [
                'status' => 'error',
                'message' => 'Database error: ' . $e->getMessage()
            ];
        }
    }
}

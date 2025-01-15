<?php

namespace App\Services;

use App\DatabaseSecondary;
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
            $stmt = $this->pdo->prepare("SELECT first_name, last_name, image, job_title FROM _users WHERE email = :email LIMIT 1");
            $stmt->bindParam(':email', $email);
            $stmt->execute();

            $userData = $stmt->fetch(PDO::FETCH_ASSOC);

            return $userData ? $userData : null;
        } catch (PDOException $e) {
            return null;
        }
    }
}

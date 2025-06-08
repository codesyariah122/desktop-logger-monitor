<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Config;

use PDO;
use PDOException;
use App\Config\SetupConstanta;

class DatabaseSecondary
{
    private static $instance = null;
    private $pdo;

    private function __construct()
    {
        SetupConstanta::init();
        $host = $_ENV['DB_HOST'];
        $dbname = $_ENV['DB_NAME_2'];
        $username = $_ENV['DB_USERNAME'];
        $password = $_ENV['DB_PASSWORD'];

        try {
            $this->pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username, $password);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }

    public static function getInstance(): self
    {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    public function getConnection(): PDO
    {
        return $this->pdo;
    }
}

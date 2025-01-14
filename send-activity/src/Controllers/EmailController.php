<?php

namespace App\Controllers;

use App\Services\LogService;

class EmailController
{
    private $logService;

    public function __construct()
    {
        $this->logService = new LogService();
    }

    public function checkEmail()
    {
        // Ambil email dari parameter GET
        $email = $_GET['email'] ?? null;

        // Cek apakah email diberikan
        if ($email) {
            // Periksa apakah email ada di database kedua
            $emailExists = $this->logService->checkEmailExistsInSecondDatabase($email);

            if ($emailExists) {
                $response = [
                    'status' => $emailExists,
                    'message' => $email . ' Email exists in members data.',
                ];
            } else {
                $response = [
                    'status' => 'error',
                    'message' => 'Email does not exist in members data.',
                ];
            }
        } else {
            $response = [
                'status' => 'error',
                'message' => 'Email parameter is missing.',
            ];
        }

        // Kirimkan respons dalam format JSON
        echo json_encode($response, JSON_PRETTY_PRINT);
    }
}

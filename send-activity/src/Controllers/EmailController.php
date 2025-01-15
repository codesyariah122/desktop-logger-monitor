<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Controllers;

use App\Services\EmailService;

class EmailController
{
    private $emailService;

    public function __construct()
    {
        $this->emailService = new EmailService();
    }

    public function checkEmail()
    {
        $email = $_GET['email'] ?? null;

        if ($email) {
            $emailExists = $this->emailService->checkEmailExistsInSecondDatabase($email);

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

        echo json_encode($response, JSON_PRETTY_PRINT);
    }

    public function handleUserData()
    {
        $email = $_GET['email'] ?? null;
        if ($email) {
            $userData = $this->emailService->getUserDataByEmail($email);

            if ($userData) {
                if (isset($userData['image'])) {
                    $imageData = unserialize($userData['image']);
                    if (isset($imageData['file_name'])) {
                        $userData['image'] = $imageData['file_name']; // Ambil nama file
                    }
                }

                $response = [
                    'status' => 'success',
                    'message' => "User data with email {$email} is existing",
                    'data' => $userData,
                ];
            } else {
                $response = [
                    'status' => 'error',
                    'message' => 'User data not found.',
                ];
            }

            echo json_encode($response, JSON_PRETTY_PRINT);
        }
    }
}

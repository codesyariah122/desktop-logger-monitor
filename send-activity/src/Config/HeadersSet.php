<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return generic
 */

namespace App\Config;

class HeadersSet
{
    public static function runHeader($name)
    {

        switch ($name) {
            case 'api':
                header("Access-Control-Allow-Origin: *");
                header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
                header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");
                header('Content-Type: application/json');
                break;
            default:
                header('Content-Type: text/html; charset=UTF-8');
        }
    }
}

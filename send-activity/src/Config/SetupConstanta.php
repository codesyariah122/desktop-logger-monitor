<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return _
 */

namespace App\Config;

use Dotenv\Dotenv;

class SetupConstanta
{
    public static function init()
    {
        $dotenv = Dotenv::createImmutable(__DIR__ . '/../..');
        $dotenv->load();
    }
}

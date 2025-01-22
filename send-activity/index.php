<?php

/**
 * @author Puji Ermanto <pujiermanto@gmail.com>
 * @return loader
 */

ini_set('display_errors', 1);
error_reporting(E_ALL);

require_once dirname(__FILE__) . '/src/index.php';

use App\Server\AgoGoConnect;

AgoGoConnect::go();

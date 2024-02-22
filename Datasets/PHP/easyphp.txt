<?php

error_reporting(0);

include 'function.php';

$dir = 'sandbox/' . sha1($_SERVER['REMOTE_ADDR'] . $_SERVER['HTTP_USER_AGENT']) . '/';

if(!file_exists($dir)){
  mkdir($dir);
}

switch ($_GET["action"] ?? "") {
  case 'pwd':
    echo $dir;
    break;
  case 'upload':
    $data = $_GET["data"] ?? "";
    if (waf($data)) {
      die('waf sucks...');
    }
    file_put_contents("$dir" . "index.php", $data);
  case 'shell':
    initShellEnv($dir);
    include $dir . "index.php";
    break;
  default:
    highlight_file(__FILE__);
    break;
}
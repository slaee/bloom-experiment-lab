<?php 
// Vulnerable code
$file = $_SERVER['DOCUMENT_ROOT'] . '/logs/log.txt';
$data = $_POST['data'];
file_put_contents($file, $data);

?> 

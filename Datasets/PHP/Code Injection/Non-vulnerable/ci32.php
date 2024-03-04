<?php 
// Remediation
$file = $_SERVER['DOCUMENT_ROOT'] . '/logs/log.txt';
$data = $_POST['data'];
$data = htmlspecialchars($data);
file_put_contents($file, $data);


?> 

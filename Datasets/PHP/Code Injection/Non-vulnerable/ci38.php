<?php 
// Remediation
$filename = $_SERVER['SCRIPT_FILENAME'];
$filename = filter_var($filename, FILTER_SANITIZE_STRING);
file_get_contents($filename);

?> 

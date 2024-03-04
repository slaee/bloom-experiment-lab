<?php 
// Vulnerable code
$filename = $_SERVER['SCRIPT_FILENAME'];
file_get_contents($filename);

?> 

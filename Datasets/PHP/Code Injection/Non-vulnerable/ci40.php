<?php 
// Remediation
$filename = $_SERVER['PHP_SELF'];
$filename = filter_var($filename, FILTER_SANITIZE_STRING);
include($filename);

?> 

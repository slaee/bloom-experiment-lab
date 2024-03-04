<?php 
// Remediation
$file = $_SERVER['PHP_SELF'];
$file = filter_var($file, FILTER_SANITIZE_STRING);
include($file);

?> 

<?php 
// Remediation
$filename = getenv('FILENAME');
$filename = filter_var($filename, FILTER_SANITIZE_STRING); // Sanitize input
include($filename);


?> 

<?php 
// Remediation
$filename = $_GET['filename'];
$filename = preg_replace('/[^a-zA-Z0-9_\-\.]/', '', $filename); // Sanitize input
include($filename);

?> 

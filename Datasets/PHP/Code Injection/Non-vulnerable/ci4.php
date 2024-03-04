<?php 
// Remediation
$filename = $_GET['filename'];
$filename = basename($filename); // Sanitize input
include($filename);

?> 
